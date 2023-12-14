# helpers/api_helpers.py
import requests
import json
from config.base_urls import BASE_URLS
from config.endpoints import ENDPOINTS
from config.auth_config import AuthConfig

class ApiHelpers:
    def __init__(self, environment='development'):
        self.base_url = BASE_URLS.get(environment, 'https://dev.example.com/')
        self.auth_token = AuthConfig.get_auth_token()
        self.custom_headers = AuthConfig.get_custom_headers()

    def get_request(self, endpoint):
        headers = self._build_headers()
        response = requests.get(url=self.base_url + endpoint, headers=headers)
        return json.loads(response.text)

    def post_request(self, endpoint, data):
        headers = self._build_headers()
        response = requests.post(url=self.base_url + endpoint, json=data, headers=headers)
        return json.loads(response.text)

    def put_request(self, endpoint, data):
        headers = self._build_headers()
        response = requests.put(url=self.base_url + endpoint, json=data, headers=headers)
        return json.loads(response.text)

    def patch_request(self, endpoint, data):
        headers = self._build_headers()
        response = requests.patch(url=self.base_url + endpoint, json=data, headers=headers)
        return json.loads(response.text)

    def delete_request(self, endpoint):
        headers = self._build_headers()
        response = requests.delete(url=self.base_url + endpoint, headers=headers)
        return response.status_code

    def _build_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'
        headers.update(self.custom_headers)
        return headers
