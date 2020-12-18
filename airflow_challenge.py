from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.dummy_operator import DummyOperator

_SCHEDULE_INTERVAL = '0 3 * * *'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    'ejercicios-airflow',
    default_args=default_args,
    description='DAG de ejercicios de airflow',
    schedule_interval=_SCHEDULE_INTERVAL,
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
