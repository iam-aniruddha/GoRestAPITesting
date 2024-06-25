import random
import string
import requests
from .config import BASE_URL, AUTH_TOKEN


def generate_random_email():
    domain = "gmail.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email


def make_get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Authorization": AUTH_TOKEN}
    response = requests.get(url, headers=headers)
    return response


def make_post_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Authorization": AUTH_TOKEN}
    response = requests.post(url, json=data, headers=headers)
    return response


def make_put_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Authorization": AUTH_TOKEN}
    response = requests.put(url, json=data, headers=headers)
    return response


def make_delete_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Authorization": AUTH_TOKEN}
    response = requests.delete(url, headers=headers)
    return response
