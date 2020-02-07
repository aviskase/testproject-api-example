import pytest
from bravado.exception import HTTPNotFound, HTTPNotAcceptable

from bravado_client.api_testproject import APITestProject


@pytest.fixture(scope='module')
def api(api_key):
    return APITestProject(api_key).client


def test_get_specific_project(api, existing_project):
    response = api.Projects.Projects_GetProject(projectId=existing_project).response()
    assert response.metadata.status_code == 200


def test_get_nonexisting_project(api):
    with pytest.raises(HTTPNotFound):
        api.Projects.Projects_GetProject(projectId='iZyZmrbAAkuHyqdB3O6fHd').response()


def test_get_specific_project_accept_html(api, existing_project):
    with pytest.raises(HTTPNotAcceptable):
        api.Projects.Projects_GetProject(
            projectId=existing_project,
            _request_options={'headers': {'Accept': 'text/html'}}
        ).response()
