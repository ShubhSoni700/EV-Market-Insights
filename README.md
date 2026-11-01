# ⚡ EV Market Insights Dashboard

### Electric Vehicle Market Performance and Technology Analysis

An interactive data analytics project designed to explore Electric Vehicle (EV) specifications, compare manufacturers, and analyze vehicle performance using Python, MySQL, Streamlit, Tableau, and Flask.

## 📌 Project Overview

The Electric Vehicle Market Insights Dashboard provides an interactive way to explore EV specifications and understand the relationship between battery capacity, driving range, efficiency, and vehicle categories.

The project uses real-world EV specification data to generate meaningful visual insights through interactive dashboards.

## ✨ Key Features

- **Manufacturer Analysis:** Explore EV models across different manufacturers.
- **Vehicle Categories:** Analyze EV distribution by body type.
- **Range Analysis:** Compare driving ranges across different vehicle categories.
- **Battery Analysis:** Explore battery capacity and its relationship with driving range.
- **Efficiency Analysis:** Understand energy consumption across EV models.
- **Interactive Filters:** Filter dashboard data by available vehicle attributes.
- **Database Integration:** Store and retrieve EV data using MySQL.
- **Web Integration:** Display the Tableau dashboard through a Flask application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and application development |
| Pandas & NumPy | Data cleaning and analysis |
| Plotly | Interactive visualizations |
| Streamlit | Interactive Python dashboard |
| MySQL | Database management |
| SQLAlchemy | Database connectivity |
| Tableau Public | Data visualization and dashboard |
| Flask | Web application integration |
| HTML & CSS | Webpage design |
| Git & GitHub | Version control |

## 📊 Dashboard Preview

**Explore the interactive Tableau dashboard:**

[View EV Market Insights Dashboard](https://public.tableau.com/views/EV_Market_Insights_17935318474090/EVMarketInsightsDashboard_)

[Visit Tableau Public Profile](https://public.tableau.com/app/profile/shubham.soni2103/vizzes)

## 📁 Project Structure

```text
EV-Market-Insights/
│
├── app.py
├── flask_app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── clean_data.py
│   ├── explore_data.py
│   ├── load_database.py
│   └── test_project.py
│
├── templates/
│   └── index.html
│
├── EV_Market_Insights.twb
└── EV_Market_Insights.twbx
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ShubhSoni700/EV-Market-Insights.git
```

### 2. Navigate to the project folder

```bash
cd EV-Market-Insights
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Install and start MySQL Server.

Create a database named:

```sql
CREATE DATABASE ev_market_db;
```

Configure your database credentials in a local `.env` file:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ev_market_db
DB_USER=root
DB_PASSWORD=your_password
```

Do not upload your `.env` file or database password to GitHub.

Run the database loading script:

```bash
python scripts/load_database.py
```

### 7. Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

### 8. Run the Flask application

```bash
python flask_app.py
```

Open the local URL displayed in your terminal, usually:

`http://127.0.0.1:5000`

## 📂 Dataset Information

**Dataset:** Electric Vehicle Specs Dataset 2025

**Source:** [Hugging Face Dataset](https://huggingface.co/datasets/UrvishAhir1/Electric-Vehicle-Specs-Dataset-2025)

**Original data source:** [EV Database](https://ev-database.org/)

**License:** CC BY 4.0

The dataset contains EV specifications such as:

- Manufacturer and model
- Battery capacity and battery type
- Driving range
- Top speed
- Energy efficiency
- Acceleration
- Charging specifications
- Vehicle dimensions and seating capacity

Dataset attribution: Urvish Ahir, Electric Vehicle Specs Dataset 2025, licensed under CC BY 4.0.

## ⚠️ Project Limitations

The current dataset primarily contains vehicle specification information. It does not provide verified historical sales figures, market share, vehicle prices, customer ratings, or complete manufacturing-location information.

Therefore, the dashboard focuses on EV specifications and performance comparisons rather than claiming actual market sales performance.

## 🎯 Project Objectives

- Understand the EV market through data analysis.
- Compare electric vehicle specifications.
- Explore battery technologies and vehicle performance.
- Develop interactive dashboards.
- Practice Python, SQL, data visualization, and web integration.

## 👨‍💻 Developer

**Shubham Soni**

GitHub: [@ShubhSoni700](https://github.com/ShubhSoni700)

Tableau Public: [Shubham Soni](https://public.tableau.com/app/profile/shubham.soni2103/vizzes)

---

⭐ If you find this project interesting, feel free to explore the repository!
