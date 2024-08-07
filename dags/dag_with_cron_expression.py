from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Lokesh',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="dag_with_cron_expression_V03",
    default_args=default_args,
    description="This is my sample DAG using cron expression",
    start_date=datetime(2024, 7, 8),
    schedule_interval='0 3 * * Tue,Fri' # 0 3 * * Tue
) as dag:
    task1 = BashOperator(
        task_id = "task1",
        bash_command="echo Dag with cron expression!"
    )
    task1