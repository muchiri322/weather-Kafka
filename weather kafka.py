import requests
import json
import pandas as pd
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def get_weather_data(**kwargs):
    url = "https://api.openweathermap.org/data/2.5/weather?q=Nakuru&appid=34af55b3fa6cdf6c4f3c642af4d74875&units=metric"
    response = requests.get(url)
    data = response.json()
    kwargs['ti'].xcom_push(key='weather_data', value=data)
    
def transform_weather_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='weather_data', task_ids='get_weather_data')
    data_main ={ 
            'weather_type': data['weather'][0]['main'],
            'Temperature': data['main']['temp'],
            'Feels_like': data['main']['feels_like'],
            'Humidity': data['main']['humidity'],
            'Pressure': data['main']['pressure'],
            'Wind_speed': data['wind']['speed'],
            'Wind_direction': data['wind']['deg'],
            'Visibility': data['visibility'],
            'Cloudiness': data['clouds']['all'],
            }
    kwargs['ti'].xcom_push(key='transformed_weather_data', value=data_main)

def load_weather_data(**kwargs):
    data_main = kwargs['ti'].xcom_pull(key='transformed_weather_data', task_ids='transform_weather_data')
    df = pd.DataFrame([data_main])
    engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
    df.to_sql('weather_data', engine, if_exists='append', index=False)
    
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    } 

  
with DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule='@daily',
    catchup=False
) as dag:
    
    get_weather_data_task = PythonOperator(
        task_id='get_weather_data',
        python_callable=get_weather_data
    )

    transform_weather_data_task = PythonOperator(
        task_id='transform_weather_data',
        python_callable=transform_weather_data
        
    )

    load_weather_data_task = PythonOperator(
        task_id='load_weather_data',
        python_callable=load_weather_data
    )

    get_weather_data_task >> transform_weather_data_task >> load_weather_data_task      
