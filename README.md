# 🌦️ Weather Data ETL Pipeline with Apache Airflow

This project is a daily **ETL (Extract, Transform, Load)** pipeline built using **Apache Airflow**. It fetches real-time weather data for **Nakuru**, Kenya from the **OpenWeatherMap API**, processes the data, and stores it in a **PostgreSQL** database for analytics and reporting.

---

## 🚀 Project Overview

- **Extract**: Retrieves current weather data from the OpenWeatherMap API.
- **Transform**: Cleans and structures the weather data using `pandas`.
- **Load**: Stores the transformed data into a PostgreSQL database table.

This pipeline runs **daily** and is orchestrated by Apache Airflow.

---

## 🛠️ Technologies Used

| Tool/Library        | Purpose                                 |
|---------------------|-----------------------------------------|
| Python              | Programming language for logic          |
| Apache Airflow      | Workflow scheduling and orchestration   |
| OpenWeatherMap API  | Source of real-time weather data        |
| Pandas              | Data transformation and structuring     |
| PostgreSQL          | Data storage                            |
| SQLAlchemy          | Python ORM for DB connectivity          |
| Requests            | HTTP client to make API calls           |

---

## 📊 Data Flow

### DAG Task Pipeline:

get_weather_data --> transform_weather_data --> load_weather_data

yaml
Copy code

- **Task 1**: `get_weather_data`  
  Calls the OpenWeatherMap API and pulls the weather data for Nakuru.

- **Task 2**: `transform_weather_data`  
  Extracts relevant fields (temperature, humidity, wind, etc.) and creates a structured dictionary.

- **Task 3**: `load_weather_data`  
  Loads the transformed weather data into a PostgreSQL table `weather_data`.

---

## 📋 Extracted & Stored Fields

| Field           | Description                        |
|----------------|------------------------------------|
| weather_type    | Main weather description (e.g. Rain) |
| Temperature     | Current temperature in °C         |
| Feels_like      | Perceived temperature in °C       |
| Humidity        | Humidity in %                     |
| Pressure        | Atmospheric pressure in hPa       |
| Wind_speed      | Wind speed in m/s                 |
| Wind_direction  | Wind direction in degrees         |
| Visibility      | Visibility in meters              |
| Cloudiness      | Cloud cover percentage (%)        |

---

## 🗃️ PostgreSQL Setup

Ensure PostgreSQL is running locally with the following configuration:

```bash
Host:     localhost  
Port:     5432  
User:     postgres  
Password: 12345  
Database: postgres
The data is appended to a table called weather_data.

🧪 Example Record
json
Copy code
{
  "weather_type": "Clear",
  "Temperature": 23.1,
  "Feels_like": 22.8,
  "Humidity": 60,
  "Pressure": 1012,
  "Wind_speed": 3.5,
  "Wind_direction": 180,
  "Visibility": 10000,
  "Cloudiness": 0
}
🧰 Getting Started
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/weather-airflow-etl.git
cd weather-airflow-etl
2. Install dependencies
bash
Copy code
pip install pandas sqlalchemy psycopg2-binary apache-airflow requests
3. Initialize Airflow
bash
Copy code
airflow db init
4. Start Airflow
bash
Copy code
airflow scheduler
airflow webserver --port 8080
Then open Airflow at: http://localhost:8080

5. Add DAG file
Place your DAG script (e.g., weather_etl_dag.py) into the Airflow dags/ directory:

bash
Copy code
cp weather_etl_dag.py ~/airflow/dags/
🔐 API Key
The project uses an API key from OpenWeatherMap:

Get your API key here

Security Tip: In production, do not hardcode the key. Store it using:

Airflow Variables

Environment variables

Secrets backends (e.g., Vault, AWS Secrets Manager)
