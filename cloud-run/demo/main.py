from flask import Flask
from google.cloud import bigquery
import pytz
import os
from datetime import datetime


TABLE = '`BIGQUERY_TABLE_NAME`'


app = Flask(__name__)


# Explicitly specify HTTP request method in order for Cloud Scheduler to invoke Cloud Run
@app.route('/', methods=['GET'])
def main():

    # Replace this function with a real job
    etl()

    return f'ETL finished'


def etl():
    """
    Demo function
    """

    # Extract
    dt_utc = datetime.now(pytz.UTC).replace(microsecond=0)

    # Transform
    dt_local = dt_utc.astimezone(tz=pytz.timezone('US/Mountain'))

    # Load
    query = f"""
        INSERT INTO {TABLE} 
            (datetime_utc, datetime_local)
        VALUES
            ('{str(dt_utc)}', '{str(dt_local)}')
    """
    bigquery.Client().query(query)

    # Printing allow us to see it in log of Cloud Run
    print(f'Ran query: {query}')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )
