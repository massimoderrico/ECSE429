
import pytest
import requests
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.todo_utils import *

@pytest.fixture()
def create_default_todo_cat_link(response, todo_cat):
    response["response"] = requests.post(
        API_URL + f"/todos/{1}/categories",
        json={"id": str(1)},
    )
    assert response["response"].status_code == 201
    todo_cat["todo_cat"] = requests.get(
        API_URL + f"/categories/{1}"
    )
    yield


@scenario('../resources/get_todo_categories.feature', 'Get all categories under a todo')
def test_get_todo_categories_normal():
    pass

@scenario('../resources/get_todo_categories.feature', 'Get no categories under a todo')
def test_get_todo_categories_alternative():
    pass

@scenario('../resources/get_todo_categories.feature', 'Get no categories under a todo')
def test_get_todo_categories_error():
    pass

# Normal Flow 


@when(
    parsers.parse("the user requests to get all categories under todo {todoID}")
)
def get_all_cat_under_todo(todoID, response, create_default_todo_cat_link):
    response["response"] = requests.get(API_URL + f"/todos/{todoID}/categories")


@then(
    parsers.parse(
        "the user will receive a list of all categories under todo {todoID}"
    )
)
def check_all_cat_under_todo(response, todo_cat):
    assert todo_cat["todo_cat"].json()["categories"]  == response["response"].json()["categories"]
  
# Alternate Flow

@then("the user will receive an empty list of categories")
def check_no_cat_under_todo(response):
    assert response["response"].json()["categories"] == []

# Error Flow

@then("the user will receive all categories under all todos")
def check_all_cat_under_invalid_todo(response, todo_cat):
    assert sorted(todo_cat["todo_cat"], key=lambda x: int(x["id"])) == sorted(
        response["response"].json()["categories"], key=lambda x: int(x["id"])
    )

