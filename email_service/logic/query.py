from urllib.request import urlopen
from urllib.parse import urljoin
from .user import User
import json
import os

BASE_URL = os.environ.get("BASE_URL")

def create_endpoint(user_id):
    data_url = urljoin(BASE_URL, str(user_id))
    return data_url

def fetch_data(endpoint, template):
    """
    This method queries the API_endpoint and returns corresponding User object
    """
    raw_user_data = urlopen(endpoint).read()
    user_data = json.loads(raw_user_data)
    user_name = user_data['data']['linkedin']['first_name']
    user_email = user_data['data']['linkedin']['email_address']
    return User(user_name, user_email, template)

def create_user(user_id, template):
    try:
        data_endpoint = create_endpoint(user_id)
        user = fetch_data(data_endpoint, template)
        return user
    except:
        print("Invalid user_id was given")
