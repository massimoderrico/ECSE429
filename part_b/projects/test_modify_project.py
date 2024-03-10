from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils_b.projects_utils import *
from conftest import *

@pytest.fixture()
def reset_database():
    # Code to set up the database goes here
    yield
    reset_default_project()

@scenario('../resources/projects/modify_project.feature', 'Modify the description of a project')
def test_modify_project_normal():
    pass

@scenario('../resources/projects/modify_project.feature', 'Modify the title of a project')
def test_modify_project_alternative():
    pass

@scenario('../resources/projects/modify_project.feature', 'Modify a project that does not exist')
def test_modify_project_error():
    pass

@when(parsers.parse('the user requests to modify the description of project "{id:d}" to "{description}"'))
def modify_project_description(id, description, context, reset_database):
    response = requests.post(API_URL + "/projects/" + str(id), json={"description": description})
    context["response"] = response

@when(parsers.parse('the user requests to modify the title of project "{id:d}" to "{title}"'))
def modify_project_title(id, title, context, reset_database):
    response = requests.post(API_URL + "/projects/" + str(id), json={"title": title})
    context["response"] = response

@when(parsers.parse('the user requests to modify a project with invalid id "{id:d}"'))
def modify_project_invalid_id(id, context, reset_database):
    response = requests.post(API_URL + "/projects/" + str(id), json={"title": ""})
    context["response"] = response


@then(parsers.parse('the user will receive the modified project object with id "{id:d}", title "{title}", and description "{description}"'))
def check_modified_project(id, title, description, context, reset_database):
    response = context["response"]
    assert response.json()["id"] == str(id)
    assert response.json()["title"] == title
    if description == '""':
        description = ''
    assert response.json()["description"] == description
    

@then(parsers.parse('the error "{error}" shall be raised with http status code "{httpstatus:d}"'))
def check_error(error, httpstatus, context, reset_database):
    response = context["response"]
    assert response.status_code == httpstatus
    assert response.json()["errorMessages"][0] == error