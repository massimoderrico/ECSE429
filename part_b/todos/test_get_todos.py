import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from utils.todo_utils import *
import requests


scenarios("../resources/get_todos.feature")

# Normal FLow

@when(parsers.parse("the user requests the todo with id {id}"))
def get_all_todo_with_id(id, response):
    response["response"] = requests.get(
        API_URL + f"/todos/{id}"
    )

@then(parsers.parse("the user will receive a todo with id {id}"))
def check_all_todo_with_id(id, response):
    filtered_response = response["response"].json()["todos"]
    filtered_todo = []
    for todo in default_todos["todos"]:
        if (todo["id"] == id):
            filtered_todo.append(todo)
            break

    assert filtered_response == filtered_todo

# #Alternate Flow

@when("the user requests to get all todos")
def get_all_todos(response):
    response["response"] = requests.get(API_URL + "/todos")

@then("the user will receive a list of all todos")
def check_all_todos(response):
    assert {
        "todos": sorted(
            response["response"].json()["todos"], key=lambda x: int(x["id"])
        )
    } == default_todos

# #Error Flow

@when(parsers.parse("the user requests to get all todos with invalid id {id}"))
def get_all_todos_invalid_id(id, response):
    response["response"] = requests.get(
        API_URL + f"/todos/{id}"
    )