
import pytest
import requests
from pytest_bdd import given, when, then, scenarios, parsers
from utils.todo_utils import *

# Define the scenario(s)
scenarios('../resources/delete_todos.feature')

# Normal Flow 

@given(parsers.parse("the todo {todoID} has a category {categoryID}"))
def create_todo_cat(todoID, categoryID, response):
    response["response"] = requests.post(
        API_URL + f"/todos/{todoID}/categories",
        json={"id": categoryID},
    )

@when(
    parsers.parse("the user requests to get all categories under todo {todoID}")
)
def get_all_projects_under_cat(todoID, response):
    response["response"] = requests.get(API_URL + f"/todos/{todoID}/categories")


@then(
    parsers.parse(
        "the user will receive a list of all projects under category {categoryID}"
    )
)
def check_projects_under_cat(categoryID, response, cat_projects):
    assert sorted(cat_projects["cat_projects"], key=lambda x: int(x["id"])) == sorted(
        response["response"].json()["projects"], key=lambda x: int(x["id"])
    )


@then("the user will receive an empty list of projects")
def check_no_project_under_cat(response):
    assert response["response"].json()["projects"] == []


@then("the user will receive all projects under all categories")
def check_projects_under_all_cat(response, cat_projects):
    assert sorted(cat_projects["cat_projects"], key=lambda x: int(x["id"])) == sorted(
        response["response"].json()["projects"], key=lambda x: int(x["id"])
    )