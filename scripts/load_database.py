
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

# Load database settings
load_dotenv()

host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Check configuration
if not all([host, database, username, password]):
    raise ValueError("Please check your .env database settings.")

# Connect to MySQL
connection_url = URL.create(
    drivername="mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

# Read cleaned EV dataset
file_path = "data/processed/cleaned_ev_data.csv"
df = pd.read_csv(file_path)

print("Dataset loaded:", df.shape)

try:
    # Test connection and clear previous imported rows
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM ev_vehicles"))

    # Import records into MySQL
    df.to_sql(
        name="ev_vehicles",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=100
    )

    # Verify imported records
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM ev_vehicles")
        )
        count = result.scalar()

    print("\nSuccessfully connected to MySQL!")
    print("Records imported:", count)
    print("Database:", database)
    print("Table: ev_vehicles")

except Exception as error:
    print("\nDatabase import failed:")
    print(error)

finally:
    engine.dispose()
