from google.cloud import dataproc_v1
from dotenv import load_dotenv
load_dotenv()


PROJECT_ID = ''
REGION = ''
CLUSTER_NAME = ''


def main():

    # Make Dataproc client
    client = dataproc_v1.ClusterControllerClient(
        client_options={'api_endpoint': f'{REGION}-dataproc.googleapis.com:443'}
    )

    # Start cluster
    try:
        client.start_cluster(
            request={
                'project_id': PROJECT_ID,
                'region': REGION,
                'cluster_name': CLUSTER_NAME
            }
        )
    except:
        print(f'Starting cluster failed')

    # Check cluster
    cluster = client.get_cluster(
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME
    )
    print(f'Cluster: {cluster.cluster_name}')
    print(f'Status: {cluster.status.state.name}')


if __name__ == '__main__':
    main()
