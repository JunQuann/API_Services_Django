from urllib.parse import urljoin
import requests
import os
import json

BASE_URL = os.environ.get('BASE_URL')

def put(image_url, auth_key, user_id):
    user_endpoint = urljoin(BASE_URL, str(user_id))
    data = {
        'user': {
            'picture_url': image_url
        }
    }
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.put(user_endpoint, data=json.dumps(data), headers=headers)
    return response.status_code
