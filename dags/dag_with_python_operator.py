from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Lokesh',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def greet(name, age):
    print(f"Hello world! My Name is {name}",
          f"And My age is {age}")

with DAG(
    dag_id="my_dag_with_python_operator_v02",
    default_args=default_args,
    description="This is my sample DAG using python operator",
    start_date=datetime(2024, 7, 31, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = "greet",
        python_callable=greet,
        op_kwargs={'name': 'Lokesh', 'age': 25}
    )

    task1