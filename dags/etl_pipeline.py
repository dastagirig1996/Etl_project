from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago
import pendulum
import sys
import os

print(os.__file__)
# from air

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from scripts.data_extraction import extract_data
from scripts.data_transmission import transform_data
from scripts.data_load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline for e-commerce data',
    schedule='@daily',
    # start_date=days_ago(1),
    start_date= pendulum.today('UTC').add(days=-1)
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_task >> transform_task >> load_task
