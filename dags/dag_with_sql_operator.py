from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner': 'Lokesh',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="dag_with_postgres_operator_V02",
    default_args=default_args,
    description="This is my sample DAG using postgres database",
    start_date=datetime(2024, 7, 8),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = SQLExecuteQueryOperator(
        task_id = "create_postgres_database",
        conn_id = 'postgres_localhost',
        sql = """
                create table if not exists dag_runs (
                    dt date,
                    dag_id character varying,
                    primary key (dt, dag_id)
                )
              """
    )

    task2 = SQLExecuteQueryOperator(
        task_id='insert_into_table',
        conn_id='postgres_localhost',
        sql="""
            insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task3 = SQLExecuteQueryOperator(
        task_id='delete_data_from_table',
        conn_id='postgres_localhost',
        sql="""
            delete from dag_runs where dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        """
    )
    task1 >> task3 >> task2