import requests


class APITestProject:
    endpoint = 'https://api.testproject.io/v2'
    auth_headers = {}

    def __init__(self, api_key=None):
        # Sometimes we don't want to authorize requests
        if api_key:
            self.auth_headers = {'Authorization': api_key}

    def _construct_headers(self, headers):
        # Allows to combine authorization header with per-request custom headers
        if isinstance(headers, dict):
            return {**self.auth_headers, **headers}
        return self.auth_headers

    def get_specific_project(self, identifier, headers=None):
        return requests.get(f'{self.endpoint}/projects/{identifier}', headers=self._construct_headers(headers))
