import json
import pprint


def main(request):

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET and POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return '', 204, headers

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    if request.method == 'GET':
        message = 'API received GET request.'
        return json.dumps({'message': message}), 200, headers

    elif request.method == 'POST':
        content_type = request.headers['content-type']
        request_body = None
        if content_type == 'application/json':
            request_body = request.get_json()['body']
        # Uploading data like CSV is text/plain
        elif content_type == 'text/plain':
            # Decode it to string data because the data is byte if text/plain
            request_body = request.data.decode('utf-8')
        message = f'API received POST request with the data: {request_body}'
        return json.dumps({'message': message}), 200, headers


if __name__ == '__main__':
    class Request:
        def __init__(self, method, body=None):
            self.method = method
            self.body = {'body': body}
            self.headers = {'content-type': 'application/json'}

        def get_json(self):
            return self.body

    request = Request(method='OPTIONS')
    pprint.pprint(main(request))
    print()
    request = Request(method='GET')
    pprint.pprint(main(request))
    print()
    request = Request(method='POST', body='test')
    pprint.pprint(main(request))
    print()
