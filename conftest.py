import pytest


@pytest.fixture(scope='session')
def api_key():
    return 'YOUR_API_KEY'


@pytest.fixture(scope='session')
def existing_project():
    return 'YOUR_PROJECT_ID'
