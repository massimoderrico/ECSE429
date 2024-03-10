from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils_b.projects_utils import *
from conftest import *

@pytest.fixture()
def reset_database_with_project_todos(scope='module'):
    yield
    delete_todo_and_relationship("Todo_1", 1)
    delete_todo_and_relationship("Todo_2", 1)

@scenario('../resources/projects/create_project_todo.feature', 'Create a project todo with only title')
def test_create_project_todo_normal():
    pass

@scenario('../resources/projects/create_project_todo.feature', 'Create a project todo specifying all fields of todo')
def test_create_project_todo_alternative():
    pass

@scenario('../resources/projects/create_project_todo.feature', 'Create a project todo without title')
def test_create_project_todo_error():
    pass

@when(parsers.parse('the user requests to create a todo with title "{title}" for project "{project_id}"'))
def create_project_todo_title(title, project_id, context, reset_database_with_project_todos):
    response = requests.post(API_URL + "/projects/" + str(project_id) + "/tasks", json={"title": title})
    context["response"] = response

@then(parsers.parse('the user will receive the created todo object with title "{title}", done status "{done_status}", and description "{description}" for project "{project_id}"'))
def check_created_project_todo(title, done_status, description, project_id, context, reset_database_with_project_todos):
    response = context["response"]
    assert response.json()["title"] == title
    assert response.json()["doneStatus"] == done_status
    if description == '""':
        description = ''
    assert response.json()["description"] == description

@when(parsers.parse('the user requests to create a todo with title "{title}", done status "{done_status}", and description "{description}" for project "{project_id}"'))
def create_project_todo_all_fields(title, done_status, description, project_id, context, reset_database_with_project_todos):
    #set done_status to a boolean from string
    if done_status == "true":
        done_status = True
    else:
        done_status = False
    response = requests.post(API_URL + "/projects/" + str(project_id) + "/tasks", json={"title": title, "doneStatus": done_status, "description": description})
    context["response"] = response


@when(parsers.parse('the user requests to create a todo for project "{project_id}" without title'))
def create_project_todo_no_title(project_id, context, reset_database_with_project_todos):
    response = requests.post(API_URL + "/projects/" + str(project_id) + "/tasks", json={"doneStatus": False, "description": "ex ea commodo consea"})
    context["response"] = response

@then(parsers.parse('the error "{error}" shall be raised with http status code "{httpstatus}"'))
def check_error_project_todo(error, httpstatus, context, reset_database_with_project_todos):
    response = context["response"]
    assert response.status_code == int(httpstatus)
    assert response.json()["errorMessages"][0] == error