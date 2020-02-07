import pytest

from requests_client.api_testproject import APITestProject


@pytest.fixture(scope='module')
def api(api_key):
    return APITestProject(api_key)


def test_get_specific_project(api, existing_project):
    response = api.get_specific_project(existing_project)
    assert response.status_code == 200


def test_get_nonexisting_project(api):
    response = api.get_specific_project('iZyZmrbAAkuHyqdB3O6fHd')
    assert response.status_code == 404


def test_get_specific_project_accept_html(api, existing_project):
    response = api.get_specific_project(existing_project, headers={'Accept': 'text/html'})
    assert response.status_code == 406
