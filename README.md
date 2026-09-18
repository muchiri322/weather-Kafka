# Weather Data Pipeline

A data engineering project that collects weather information from the OpenWeather API, processes the data using Python and Pandas, and stores the transformed data in PostgreSQL.

The project uses Apache Airflow to orchestrate and schedule the ETL workflow.

## Project Overview

```text
OpenWeather API
       |
       v
    Extract
       |
       v
    Transform
       |
       v
     Load
       |
       v
   PostgreSQL
```

## Technologies Used

- Python
- Apache Airflow
- OpenWeather API
- Pandas
- Requests
- SQLAlchemy
- PostgreSQL

## Pipeline Workflow

### 1. Extract

The pipeline requests weather data from the OpenWeather API. The response contains weather condition, temperature, feels-like temperature, humidity, pressure, wind speed, wind direction, visibility, and cloudiness.

### 2. Transform

The raw API response is transformed into a structured record containing:

```text
weather_type
Temperature
Feels_like
Humidity
Pressure
Wind_speed
Wind_direction
Visibility
Cloudiness
```

Airflow XCom is used to pass the data between tasks.

### 3. Load

The transformed record is converted to a Pandas DataFrame and loaded into PostgreSQL using SQLAlchemy.

Destination table:

```text
weather_data
```

## Airflow DAG

The DAG is named:

```text
weather_data_pipeline
```

It runs daily with:

```text
@daily
```

Task dependency:

```text
get_weather_data
        |
        v
transform_weather_data
        |
        v
load_weather_data
```

## Project Structure

```text
weather-kafka/
│
├── dags/
│   └── weather_data_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

Do not hardcode API keys or database credentials in source code.

Example:

```text
OPENWEATHER_API_KEY=your_api_key
DATABASE_URL=postgresql://username:password@host:port/database
```

Never commit `.env` files, API keys, passwords, or connection strings to GitHub.

## Running with Airflow

Initialize Airflow:

```bash
airflow db migrate
```

Start the scheduler:

```bash
airflow scheduler
```

Start the webserver in another terminal:

```bash
airflow webserver
```

Then enable `weather_data_pipeline` in the Airflow web interface.

## Data Engineering Concepts Demonstrated

- REST API extraction
- ETL pipeline development
- Pandas data transformation
- PostgreSQL loading
- SQLAlchemy
- Apache Airflow DAGs
- Airflow XCom
- Task dependencies
- Pipeline scheduling
- Environment-variable based configuration

## Kafka Extension

The current pipeline code is an Airflow + OpenWeather API + PostgreSQL ETL workflow. Kafka is not implemented in the uploaded code yet.

A Kafka version can extend the architecture to:

```text
OpenWeather API
       |
       v
Apache Airflow
       |
       v
Kafka Producer
       |
       v
Kafka Topic
       |
       v
Kafka Consumer
       |
       v
PostgreSQL
```

Future improvements can include Kafka producers and consumers, historical weather storage, streaming processing, data quality checks, Grafana monitoring, and Docker deployment.



## Author

**Muchiri**

Data Engineer | Data Analyst | AI/ML

GitHub: https://github.com/muchiri322
