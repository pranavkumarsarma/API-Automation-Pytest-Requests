import json
import os
import pytest
from config.base_urls import BASE_URLS
from config.endpoints import ENDPOINTS
from helpers.api_helpers import ApiHelpers

@pytest.fixture
def api(request):
    environment = os.environ.get("ENVIRONMENT", "development")
    return ApiHelpers(environment)

def load_user_data(file_path):
    with open(file_path, "r") as file:
        user_data = json.load(file)
    return user_data

@pytest.mark.parametrize("user_id, expected_name", [(2, "Janet"), (3, "Emma")], ids=["User ID 2", "User ID 3"])
def test_fetch_user(api, user_id, expected_name):
    endpoint = ENDPOINTS['users']
    response_json = api.get_request(endpoint)
    print(response_json)
    # Check if 'data' key exists in the response
    assert 'data' in response_json, "Response does not contain 'data' key"
    # Assume each item in the list has an "id" field
    users = response_json['data']
    user = next((user for user in users if user.get("id") == user_id), None)
    # Assert if the user is found and has the expected name
    assert user is not None, f"User with ID {user_id} not found in the response"
    assert user.get("first_name") == expected_name

@pytest.mark.parametrize("user_data_file", ["TestData/user1.json", "TestData/user2.json"])
def test_create_user(api, user_data_file):
    endpoint = ENDPOINTS['users']
    user_data = load_user_data(user_data_file)
    response_json = api.post_request(endpoint, user_data)
    print(response_json)
    assert response_json["name"] is not None
    assert response_json["id"] is not None
    assert response_json["createdAt"] is not None
    assert response_json["job"] == user_data["job"]


@pytest.mark.parametrize("user_data_file", ["TestData/user1.json", "TestData/user2.json"])
def test_update_user(api, user_data_file):
    user_id_to_update = 1  # Assuming there is an existing user with ID 1
    endpoint = f"{ENDPOINTS['users']}/{user_id_to_update}"
    
    user_data = load_user_data(user_data_file)
    
    # Perform a PUT request to update the user
    response_json = api.put_request(endpoint, user_data)
    
    print(response_json)
    assert response_json["name"] is not None
    assert response_json["id"] == user_id_to_update
    assert response_json["updatedAt"] is not None
    assert response_json["job"] == user_data["job"]

@pytest.mark.parametrize("user_data_file", ["TestData/user1.json", "TestData/user2.json"])
def test_patch_user(api, user_data_file):
    user_id_to_patch = 1  # Assuming there is an existing user with ID 1
    endpoint = f"{ENDPOINTS['users']}/{user_id_to_patch}"
    
    user_data = load_user_data(user_data_file)
    
    # Perform a PATCH request to update the user
    response_json = api.patch_request(endpoint, user_data)
    
    print(response_json)
    assert response_json["name"] is not None
    assert response_json["id"] == user_id_to_patch
    assert response_json["updatedAt"] is not None
    assert response_json["job"] == user_data["job"]


@pytest.mark.parametrize("user_id_to_delete", [4, 5, 6])
def test_delete_user(api, user_id_to_delete):
    endpoint = ENDPOINTS['users'] + str(user_id_to_delete)
    response_status_code = api.delete_request(endpoint)
    assert response_status_code == 204  # Assuming successful deletion, double verification


# Add more test functions as needed for other endpoints and scenarios
