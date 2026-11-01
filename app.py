
import os
import pandas as pd
import streamlit as st
import plotly.express as px

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Page configuration
st.set_page_config(
    page_title="EV Market Insights",
    page_icon="⚡",
    layout="wide"
)

# Load database credentials
load_dotenv()

st.title("⚡ Electric Vehicle Market Performance & Insights")
st.caption("Interactive Electric Vehicle Specifications Dashboard")

# Connect to MySQL
@st.cache_data(ttl=60)
def load_data():
    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME", "ev_market_db")
    )

    engine = create_engine(connection_url)

    try:
        df = pd.read_sql("SELECT * FROM ev_vehicles", engine)
    finally:
        engine.dispose()

    return df


try:
    df = load_data()

    if df.empty:
        st.warning("No EV records found in the database.")
        st.stop()

    # Sidebar filters
    st.sidebar.header("Dashboard Filters")

    brands = sorted(df["brand"].dropna().unique())
    selected_brands = st.sidebar.multiselect(
        "Select Manufacturers",
        brands,
        default=brands
    )

    body_types = sorted(df["car_body_type"].dropna().unique())
    selected_bodies = st.sidebar.multiselect(
        "Select Vehicle Body Types",
        body_types,
        default=body_types
    )

    filtered_df = df[
        df["brand"].isin(selected_brands)
        & df["car_body_type"].isin(selected_bodies)
    ].copy()

    if filtered_df.empty:
        st.warning("No vehicles match these filters.")
        st.stop()

    # KPI cards
    st.subheader("Market Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total EV Models", len(filtered_df))
    col2.metric(
        "Manufacturers",
        filtered_df["brand"].nunique()
    )
    col3.metric(
        "Average Range",
        f"{filtered_df['range_km'].mean():.0f} km"
    )
    col4.metric(
        "Average Battery",
        f"{filtered_df['battery_capacity_kWh'].mean():.1f} kWh"
    )

    st.divider()

    # Manufacturer analysis
    st.subheader("1. Manufacturer Analysis")

    brand_counts = (
        filtered_df.groupby("brand")
        .size()
        .reset_index(name="models")
        .sort_values("models", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        brand_counts,
        x="brand",
        y="models",
        color="models",
        title="Top 10 Manufacturers by Number of Models",
        labels={"brand": "Manufacturer", "models": "EV Models"}
    )

    st.plotly_chart(fig1, use_container_width=True)

    # Vehicle body analysis
    col5, col6 = st.columns(2)

    with col5:
        body_counts = (
            filtered_df["car_body_type"]
            .value_counts()
            .reset_index()
        )
        body_counts.columns = ["Body Type", "Count"]

        fig2 = px.pie(
            body_counts,
            names="Body Type",
            values="Count",
            title="EV Distribution by Body Type",
            hole=0.4
        )

        st.plotly_chart(fig2, use_container_width=True)

    with col6:
        body_range = (
            filtered_df.groupby("car_body_type")["range_km"]
            .mean()
            .reset_index()
        )

        fig3 = px.bar(
            body_range,
            x="car_body_type",
            y="range_km",
            title="Average Range by Body Type",
            labels={
                "car_body_type": "Body Type",
                "range_km": "Average Range (km)"
            }
        )

        st.plotly_chart(fig3, use_container_width=True)

    # Battery analysis
    st.subheader("2. Battery Performance Analysis")

    fig4 = px.scatter(
        filtered_df,
        x="battery_capacity_kWh",
        y="range_km",
        color="car_body_type",
        hover_name="model",
        hover_data=["brand", "battery_type"],
        title="Battery Capacity vs Driving Range",
        labels={
            "battery_capacity_kWh": "Battery Capacity (kWh)",
            "range_km": "Driving Range (km)"
        }
    )

    st.plotly_chart(fig4, use_container_width=True)

    # Top range vehicles
    st.subheader("3. Top 10 EV Models by Driving Range")

    top_range = filtered_df.nlargest(10, "range_km")[
        ["brand", "model", "range_km", "battery_capacity_kWh"]
    ]

    st.dataframe(top_range, use_container_width=True)

    # Efficiency analysis
    st.subheader("4. Energy Efficiency Analysis")

    fig5 = px.bar(
        filtered_df.nlargest(15, "range_km"),
        x="model",
        y="efficiency_wh_per_km",
        color="brand",
        title="Energy Consumption of 15 Long-Range EV Models",
        labels={
            "model": "EV Model",
            "efficiency_wh_per_km": "Energy Consumption (Wh/km)"
        }
    )

    st.plotly_chart(fig5, use_container_width=True)

    # Raw data
    with st.expander("View Complete EV Dataset"):
        st.dataframe(filtered_df, use_container_width=True)

    st.success("Dashboard loaded successfully!")

except Exception as error:
    st.error("Unable to load the dashboard.")
    st.exception(error)
