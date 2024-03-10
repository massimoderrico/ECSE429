from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils.utils import *
from utils.projects_utils import *

@given("the API is responsive")
def valid_api():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"

@then(parsers.parse('the status code "{status_code}" will be received'))
def check_status_code(status_code, context):
    response = context["response"]
    assert response.status_code == int(status_code)

@given("the database contains the default project objects")
def get_default_projects():
    response = requests.get(API_URL + "/projects")
    assert response.status_code == 200
    modified_response = response.json()
    for project in modified_response['projects']:
        project['tasks'] = sorted(project['tasks'], key=lambda x: int(x['id']))
    assert modified_response == default_projects