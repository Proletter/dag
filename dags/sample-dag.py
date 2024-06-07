from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello from Azure Data Factory Apache Airflow!")

with DAG(
    "sample_dag",
    start_date=datetime(2024, 6, 7),
    schedule_interval=None,
    catchup=False
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello
    )