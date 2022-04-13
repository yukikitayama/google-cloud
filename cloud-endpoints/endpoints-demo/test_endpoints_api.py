import requests
import json


URL = 'CLOUD_ENDPOINTS_URL_AND_PATH'
API_KEY = 'API_KEY'


def main():

    # Make HTTP GET request
    r = requests.request(
        method='GET',
        url=URL,
        headers={
            'Content-Type': 'application/json'
        }
    )
    print('GET request')
    print(f'Status code: {r.status_code}')
    print(f'Response: {r.json()}')
    print()

    # Make HTTP POST request without API key
    # This fails because POST method requires authentication by API key
    r = requests.request(
        method='POST',
        url=URL,
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'body': 'This is test data'
        })
    )
    print('POST request without API key')
    print(f'Status code: {r.status_code}')
    print(f'Response: {r.json()}')
    print()

    # POST request is successful if supplying API key
    r = requests.request(
        method='POST',
        url=f'{URL}?key={API_KEY}',
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'body': 'This is test data'
        })
    )
    print('POST request with API key')
    print(f'Status code: {r.status_code}')
    print(f'Response: {r.json()}')
    print()


if __name__ == '__main__':
    main()
