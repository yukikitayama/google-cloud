from google.cloud import dataproc_v1


PROJECT_ID = ''
REGION = 'us-central1'
CLUSTER_NAME = 'demo'


def main(request):

    # Make Dataproc client
    client = dataproc_v1.ClusterControllerClient(
        client_options={'api_endpoint': f'{REGION}-dataproc.googleapis.com:443'}
    )

    # Start cluster
    result = client.start_cluster(
        request={
            'project_id': PROJECT_ID,
            'region': REGION,
            'cluster_name': CLUSTER_NAME
        }
    )
    print(result)


if __name__ == '__main__':
    main('')
