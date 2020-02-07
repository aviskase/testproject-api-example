import json
from pathlib import Path

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient


class APITestProject:
    host = 'api.testproject.io'
    swagger_spec = 'https://api.testproject.io/docs/v2/swagger.json'
    swagger_file = Path(__file__).parent / 'swagger.json'

    def __init__(self, api_key=None):
        http_client = RequestsClient()
        if api_key:
            http_client.set_api_key(self.host, api_key, param_name='Authorization', param_in='header')
        # Usually I'll use `from_url` generation, but current version of specification is not valid OpenAPI 2.0
        # self.client = SwaggerClient.from_url(self.swagger_spec, http_client=http_client)
        swagger_spec = json.load(self.swagger_file.open())
        self.client = SwaggerClient.from_spec(swagger_spec, http_client=http_client)
