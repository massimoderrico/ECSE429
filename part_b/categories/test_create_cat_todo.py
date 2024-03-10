import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from utils.cat_utils import *


scenarios("../resources/create_cat_todo.feature")


@when(
    parsers.parse(
        "the user requests to create a todo with title {title} under category {categoryID}"
    )
)
def create_simple_cat_todo(title, categoryID, response):
    response["response"] = requests.post(
        API_URL + f"/categories/{categoryID}/todos",
        json={"title": title},
    )


@then(
    parsers.parse(
        "the user will receive the created todo object with title {title}, done status {doneStatus}, and description {description}"
    )
)
def check_created_cat_todo(title, doneStatus, description, response):
    cat_todo = response["response"].json()
    assert cat_todo["title"] == title
    assert cat_todo["doneStatus"] == doneStatus
    # Need to remove "" since no empty string symbol
    assert cat_todo["description"] == description.replace('"', "")


@when(
    parsers.parse(
        "the user requests to create a todo with title {title},  done status {doneStatus}, and description {description} under category {categoryID}"
    )
)
def create_complete_cat_todo(title, doneStatus, description, categoryID, response):
    response["response"] = requests.post(
        API_URL + f"/categories/{categoryID}/todos",
        json={
            "title": title,
            # DoneStatus should be a boolean
            "doneStatus": True if doneStatus.lower() == "true" else False,
            "description": description,
        },
    )


@when(
    parsers.parse("the user requests to create a todo with under category {categoryID}")
)
def create_cat_todo_no_title(categoryID, response):
    response["response"] = requests.post(
        API_URL + f"/categories/{categoryID}/todos",
        json={},
    )
