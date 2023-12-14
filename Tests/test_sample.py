# tests/test_api.py
import json
import pytest
from config.base_urls import BASE_URLS
from config.endpoints import ENDPOINTS
from helpers.api_helpers import ApiHelpers

@pytest.fixture
def api(request):
    environment = request.config.getoption("--env") or 'development'
    return ApiHelpers(environment)

@pytest.mark.parametrize("user_id, expected_name", [(2, "Janet"),(3,"John")])
def test_fetch_user(api, user_id, expected_name):
    endpoint = ENDPOINTS['users']
    response_json = api.get_request(endpoint)
    assert response_json["data"]["first_name"] == expected_name
    assert response_json["data"]["id"] == user_id