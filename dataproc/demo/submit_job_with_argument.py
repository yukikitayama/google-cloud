from google.cloud import dataproc_v1
from dotenv import load_dotenv
load_dotenv()


PROJECT_ID = ''
REGION = ''
CLUSTER_NAME = ''
# Python script gsutil URI in Cloud Storage
MAIN_PYTHON_FILE_URI = ''


def main():

    # Make Dataproc client
    client = dataproc_v1.JobControllerClient(
        client_options={
            'api_endpoint': f'{REGION}-dataproc.googleapis.com:443'
        }
    )

    # Submit a job
    job = {
        'placement': {
            'cluster_name': CLUSTER_NAME
        },
        'pyspark_job': {
            'main_python_file_uri': MAIN_PYTHON_FILE_URI,
            'args': ['test', '1']
        }
    }
    result = client.submit_job(
        request={
            'project_id': PROJECT_ID,
            'region': REGION,
            'job': job
        }
    )
    job_id = result.reference.job_id
    print(f'Submitted job ID: {job_id}')


if __name__ == '__main__':
    main()
