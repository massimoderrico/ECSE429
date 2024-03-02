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
def create_todo(todo):
    response = requests.post(
        API_URL + "/todos",
        json={"title": todo_name, "description": todo_desc},
    )
    todo.title = 


@then('a new todo exists in the database with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" ')
def check_created_todo(todo):





## clean up after 