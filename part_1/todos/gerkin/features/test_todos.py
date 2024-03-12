import pytest
import requests
from pytest_bdd import given, when, then, scenarios, parsers
from helper_classes import *
from utils.utils_todos import *

# Define the scenario(s)
scenarios('todos.feature')

@pytest.fixture
def todo():
    return Todo()

# Step definitions
@given('the database contains the following todos:')
def default_state():
    pass

@when('a new todo is created with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>"')
def create_todo(todo, todo_name, todo_done_status, todo_desc):
    response = requests.post(
        API_URL + "/todos",
        json={"title": todo_name,"doneStatus": todo_done_status ,"description": todo_desc},
    )
    todo.title = response["title"]
    todo.doneStatus = response["doneStatus"]
    todo.description = response["description"]

@then('a new todo exists in the database with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" ')
def check_created_todo(todo, todo_name, todo_done_status, todo_desc):
    assert todo.title == todo_name
    assert todo.doneStatus == todo_done_status
    assert todo.description == todo_desc


@pytest.hookimpl
def pytest_bdd_after_scenario(request, feature, scenario, result):
    print("After scenario:", scenario.name)


## clean up after 