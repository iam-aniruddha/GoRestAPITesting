import pytest
import json
from utils.helper_functions import generate_random_email, make_get_request, make_post_request, make_put_request, make_delete_request


def test_get_users():
    response = make_get_request("/public/v2/users/")
    assert response.status_code == 200
    json_data = response.json()
    print("json GET request response body: ", json.dumps(json_data, indent=4))
    print("********************DONE**********************")


def test_create_user():
    data = {
        "name": "Test Name",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = make_post_request("/public/v2/users/", data)
    assert response.status_code == 201
    json_data = response.json()
    print("json POST request response body: ", json.dumps(json_data, indent=4))
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Test Name"
    print("********************DONE**********************")
    return user_id


def test_update_user():
    user_id = test_create_user()
    data = {
        "name": "Updated Test Name",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = make_put_request(f"/public/v2/users/{user_id}", data)
    assert response.status_code == 200
    json_data = response.json()
    print("json PUT request response body: ", json.dumps(json_data, indent=4))
    assert json_data["id"] == user_id
    assert json_data["name"] == "Updated Test Name"
    print("********************DONE**********************")


def test_delete_user():
    user_id = test_create_user()
    response = make_delete_request(f"/public/v2/users/{user_id}")
    assert response.status_code == 204
    print("........DELETE USER IS DONE...........")
    print("********************DONE**********************")
