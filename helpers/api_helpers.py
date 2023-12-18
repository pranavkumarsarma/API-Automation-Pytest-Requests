# helpers/api_helpers.py
import requests
import json
from config.base_urls import BASE_URLS
from config.endpoints import ENDPOINTS
from config.auth_config import AuthConfig

class ApiHelpers:
    def __init__(self, environment='development'):
        self.base_url = BASE_URLS.get(environment, 'https://dev.example.com/')
        #self.auth_token = AuthConfig.get_auth_token()
        #self.custom_headers = AuthConfig.get_custom_headers()

    def get_request(self, endpoint):
        response = requests.get(url=self.base_url + endpoint)
        assert response.status_code == 200, f"GET request failed with status code {response.status_code}"

        try:
            # Try to parse the response as JSON
            response_json = response.json()
        except json.JSONDecodeError:
            # If parsing fails, assume it's not JSON and return None
            return None

        return response_json

    def post_request(self, endpoint, data):
       # headers = self._build_headers()
       # response = requests.post(url=self.base_url + endpoint, json=data, headers=headers)
        response = requests.post(url=self.base_url + endpoint, json=data)
        assert response.status_code == 201, f"POST request failed with status code {response.status_code}"
        return json.loads(response.text)

    def put_request(self, endpoint, data):
        # headers = self._build_headers()
        response = requests.put(url=self.base_url + endpoint, json=data)
        assert response.status_code == 200, f"PUT request failed with status code {response.status_code}"
        return json.loads(response.text)

    def patch_request(self, endpoint, data):
        # headers = self._build_headers()
        response = requests.patch(url=self.base_url + endpoint, json=data)
        assert response.status_code == 200, f"PATCH request failed with status code {response.status_code}"
        return json.loads(response.text)

    def delete_request(self, endpoint):
        # headers = self._build_headers()
        response = requests.delete(url=self.base_url + endpoint)
        assert response.status_code == 204, f"DELETE request failed with status code {response.status_code}"
        return response.status_code

    # def _build_headers(self):
    #     headers = {'Content-Type': 'application/json'}
    #     if self.auth_token:
    #       headers['Authorization'] = f'Bearer {self.auth_token}'
    #     if self.custom_headers:
    #       headers.update(self.custom_headers)
    #     return headers
