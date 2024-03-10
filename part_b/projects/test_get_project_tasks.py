from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils_b.projects_utils import *
from conftest import *


@pytest.fixture()
def reset_database_with_project(scope='module'):
    yield
    # get id of project with title
    response_temp = requests.get(API_URL + "/projects", params={"title": "Office Work II"})
    #get id
    id_temp = response_temp.json()["projects"][0]["id"]
    delete_project(id_temp)
    

@scenario('../resources/projects/get_project_tasks.feature', 'Get all tasks for a project')
def test_get_project_tasks_normal():
    pass

@scenario('../resources/projects/get_project_tasks.feature', 'Get no tasks for a project')
def test_get_project_tasks_alternative():
    pass

@scenario('../resources/projects/get_project_tasks.feature', 'Get all tasks for a project that does not exist')
def test_get_project_tasks_error():
    pass

# Background
@given(parsers.parse('the database contains project with no tasks with title "Office Work II" and description "Work in the office" and completed "false" and active "false"'))
def step_db_contains_project_with_no_tasks(reset_database_with_project):
    create_project("Office Work II", "Work in the office")

# Normal Flow
@when(parsers.parse('the user requests all tasks for project "{id}"'))
def step_user_requests_all_tasks_for_project(context, id, reset_database_with_project):
    response = requests.get(API_URL + "/projects/" + id + "/tasks")
    context["response"] = response


@then(parsers.parse('the user will receive a list of all tasks for project "{id}"'))
def step_user_receives_all_tasks_for_project(context, id, reset_database_with_project):
    response = context["response"]
    sorted_todos = sorted(response.json()["todos"], key=lambda x: x["id"])
    assert sorted_todos == sorted(default_project_tasks["todos"], key=lambda x: x["id"])

# Alternate Flow
@when(parsers.parse('the user requests all tasks for project with title "{title}"'))
def step_user_requests_all_tasks_for_project_with_title(context, title, reset_database_with_project):
    # get id of project with title
    response = requests.get(API_URL + "/projects", params={"title": title})
    #get id
    id = response.json()["projects"][0]["id"]
    #get project with id
    response = requests.get(API_URL + "/projects/" + str(id))
    context["response"] = response

@then('the user will receive an empty list of tasks')
def step_user_receives_empty_list_of_tasks(context, reset_database_with_project):
    response = context["response"]
    tasks = {'todos': []}
    
    for key in response.json():
        if key == 'tasks':
            tasks['todos'] = response.json()[key]
    
    assert {'todos': []} == empty_todos
