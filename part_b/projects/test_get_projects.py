from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils_b.projects_utils import *
from conftest import *

@scenario('../resources/projects/get_projects.feature', 'Get all projects')
def test_get_projects_normal():
    pass

@scenario('../resources/projects/get_projects.feature', 'Get all projects matching a title')
def test_get_projects_alternative():
    pass

@scenario('../resources/projects/get_projects.feature', 'Get all projects matching an invalid project ID')
def test_get_projects_error():
    pass

@when("the user requests to get all projects")
def request_projects(context):
    response = requests.get(API_URL + "/projects")
    context["response"] = response

@then("the user will receive a list of all projects")
def check_project_list(context):
    response = context["response"]
    modified_response = response.json()
    for project in modified_response['projects']:
        project['tasks'] = sorted(project['tasks'], key=lambda x: int(x['id']))
    assert modified_response == default_projects

@when(parsers.parse('the user requests to get all projects with title "{title}"'))
def request_projects_title(title, context):
    response = requests.get(API_URL + "/projects", params={"title": title})
    context["response"] = response

@then(parsers.parse('the user will receive a list of all projects with title "{title}"'))
def check_project_title_list(title, context):
    response = context["response"]
    modified_response = response.json()
    for project in modified_response['projects']:
        project['tasks'] = sorted(project['tasks'], key=lambda x: int(x['id']))
    assert modified_response == default_projects

@when(parsers.parse('the user requests to get all projects with an invalid id "{id}"'))
def request_projects_invalid_id(id, context):
    response = requests.get(API_URL + "/projects", params={"id": id})
    context["response"] = response

@then('the user will receive an empty list of projects')
def check_empty_list(context):
    response = context["response"]
    assert response.status_code == 200
    assert response.json() == empty_projects

    