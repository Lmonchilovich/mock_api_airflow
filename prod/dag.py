from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 26),
    'retries': 0
}

dag = DAG(
    'mock_api_data_pipeline',
    default_args=default_args,
    description='Runs an external Python script to load mock data into cloud storage',
    schedule_interval='@daily',
    catchup=False
)

with dag:
    run_script_task = BashOperator(
        task_id = 'run_script',
        bash_command='python3 /home/airflow/gcs/dags/scripts/api_request.py'
    )