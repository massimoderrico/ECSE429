import pytest
from pytest_bdd import given, scenario, then, when, parsers
from utils.todo_utils import *
from conftest import *
import requests

@pytest.fixture()
def reset_modify_todo():
    yield 
    reset_default_todo_values("scan paperwork", "", 1)

 

@scenario('../resources/modify_todo.feature', 'Modify the description of a todo')
def test_modify_todo_normal():
    pass

@scenario('../resources/modify_todo.feature', 'Modify the title of a todo')
def test_modify_todo_alternative():
    pass

@scenario('../resources/modify_todo.feature', 'Modify a todo with an invalid todo ID')
def test_modify_todo_error():
    pass

#Normal Flow

@when(
    parsers.parse(
        "the user requests to modify the description of todo {id} to description {description}"
    )
)
def modify_todo_desc(id, description, response):
    response["response"] = requests.post(
        API_URL + f"/todos/{id}",
        json={"description": description}
    )

@then(
    parsers.parse(
        "the user will receive the modified todo object with id {id} and description {description}"
    )
)
def check_todo_desc(id, description, response):
    todo = response["response"].json()
    assert todo["id"] == str(id)
    assert todo["description"] == description

@then("the todo is reset")
def reset_todo():
    reset_default_todo_values("scan paperwork", "", 1)
# Alternate Flow 
    
@when(
    parsers.parse(
        "the user requests to modify the title of todo {id} to title {title}"
    )
)

def when_modify_todo_title(id, title, response):
    response["response"] = requests.post(
        API_URL + "/todos/" + str(id),
        json={"title": title},
    )


@then(
    parsers.parse(
        "the user will receive the modified todo object with id {id} and title {title}"
    )
)
def check_todo_title(id, title, response):
    todo = response["response"].json()
    assert todo["id"] == str(id)
    assert todo["title"] == title

# # Error Flow

@when(parsers.parse("the user requests to modify a todo with invalid id {id}"))
def when_modify_invalid_id(id, response):
    response["response"] = requests.post(
        API_URL + "/todos/" + str(id),
        json={}
    )

