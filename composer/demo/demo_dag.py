"""
- Set the following environment variable in Composer
  - SLACK_TOKEN: bot-user-oauth-token
"""


from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests
import os


# Composer automatically create Cloud Storage bucket
# which is accessible from Airflow
# /home/airflow/gcs/dags is 'dags' folder by default created in the bucket
# We will also have 'data' folder in the Cloud Storage bucket by default
# Place this dag python code in dags folder, and place other Python code
# which are used in BashOperator in data folder
DAG_ID = 'demo'
HOME = f'/home/airflow/gcs/data/{DAG_ID}'
CHANNEL = '#webapp'


# Define a helper function
def message_to_slack(text):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {os.environ["SLACK_TOKEN"]}'
    }
    payload = {
        'channel': CHANNEL,
        'text': text
    }
    r = requests.post(
        url='https://slack.com/api/chat.postMessage',
        headers=headers,
        params=payload
    )
    print(f'Status code: {r.status_code}')
    print(f'Response: {r.json()}')


with DAG(
    dag_id=DAG_ID,
    default_args={
        'owner': 'Yuki',
        'retries': 0
    },
    description='This is a demo DAG',
    # Every 5 minutes
    schedule_interval='0 * * * *',
    start_date=days_ago(0),
    tags=['demo']
) as dag:

    # Define tasks
    task1 = BashOperator(
        task_id='task_a',
        bash_command=f'python {HOME}/task_a.py'
    )

    task2 = PythonOperator(
        task_id='slack_task_a_success',
        python_callable=message_to_slack,
        op_kwargs={
            'text': 'Task A finished successfully'
        },
        trigger_rule='all_success'
    )

    task3 = BashOperator(
        task_id='task_b',
        bash_command=f'python {HOME}/task_b.py',
        trigger_rule='all_done'
    )

    task4 = PythonOperator(
        task_id='slack_task_b_failed',
        python_callable=message_to_slack,
        op_kwargs={
            'text': 'Task B failed'
        },
        trigger_rule='all_failed'
    )

    # Set task dependency
    task1 >> [task2, task3]
    task3 >> task4
