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

# def test_create_user(api):
#     endpoint = ENDPOINTS['users']
#     user_data = {
#         "first_name": "New",
#         "last_name": "User",
#         "email": "new.user@example.com"
#     }
#     response_json = api.post_request(endpoint, user_data)
#     assert response_json["data"]["id"] is not None
#     assert response_json["data"]["first_name"] == "New"
#     assert response_json["data"]["last_name"] == "User"
#     assert response_json["data"]["email"] == "new.user@example.com"

# def test_update_user(api):
#     user_id = 1  # Assuming there is an existing user with ID 1
#     endpoint = ENDPOINTS['users'] + str(user_id)
#     updated_data = {
#         "first_name": "Updated",
#         "last_name": "User",
#         "email": "updated.user@example.com"
#     }
#     response_json = api.put_request(endpoint, updated_data)
#     assert response_json["data"]["id"] == user_id
#     assert response_json["data"]["first_name"] == "Updated"
#     assert response_json["data"]["last_name"] == "User"
#     assert response_json["data"]["email"] == "updated.user@example.com"

# def test_partial_update_user(api):
#     user_id = 1  # Assuming there is an existing user with ID 1
#     endpoint = ENDPOINTS['users'] + str(user_id)
#     partial_data = {
#         "last_name": "UpdatedLastName"
#     }
#     response_json = api.patch_request(endpoint, partial_data)
#     assert response_json["data"]["id"] == user_id
#     assert response_json["data"]["last_name"] == "UpdatedLastName"

# def test_delete_user(api):
#     user_id_to_delete = 4  # Assuming there is an existing user with ID 4
#     endpoint = ENDPOINTS['users'] + str(user_id_to_delete)
#     response_status_code = api.delete_request(endpoint)
#     assert response_status_code == 204  # Assuming successful deletion 

# Add more test functions as needed for other endpoints and scenarios
