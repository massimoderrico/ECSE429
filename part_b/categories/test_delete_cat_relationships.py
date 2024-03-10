import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from utils.cat_utils import *


scenarios("../resources/delete_cat_relationships.feature")


@given(
    parsers.parse(
        "the database contains the category todo with title {title}, done status {doneStatus}, and description {description} under category {categoryID}"
    )
)
def create_cat_todo(title, description, doneStatus, categoryID, cat_todos):
    response = requests.post(
        API_URL + f"/categories/{categoryID}/todos",
        json={
            "title": title,
            # DoneStatus should be a boolean
            "doneStatus": True if doneStatus.lower() == "true" else False,
            "description": description,
        },
    )
    assert response.status_code == 201
    cat_todos["cat_todos"].append(response.json())


@given(
    parsers.parse(
        "the database contains the category project title {title} and description {description} under category {categoryID}"
    )
)
def create_cat_project(title, description, categoryID, cat_projects):
    response = requests.post(
        API_URL + f"/categories/{categoryID}/projects",
        json={
            "title": title,
            "description": description,
        },
    )
    assert response.status_code == 201
    cat_projects["cat_projects"].append(response.json())


@when(parsers.parse("the user requests to delete the todo under category {categoryID}"))
def when_delete_cat_todo(categoryID, cat_todos, response):
    response["response"] = requests.delete(
        API_URL + f"/categories/{categoryID}/todos/{cat_todos['cat_todos'][0]['id']}"
    )


@then(
    parsers.parse("the status code {status_code} will be received with the text {text}")
)
def check_status_code_and_text(status_code, text, response):
    assert response["response"].status_code == int(status_code)
    assert response["response"].text == text.replace('"', "")


@when(
    parsers.parse("the user requests to delete the project under category {categoryID}")
)
def when_delete_cat_project(categoryID, cat_projects, response):
    response["response"] = requests.delete(
        API_URL
        + f"/categories/{categoryID}/projects/{cat_projects['cat_projects'][0]['id']}"
    )


@when(
    parsers.parse(
        "the user requests to delete the todo with invalid ID {invalid_todo_ID} under the category {categoryID}"
    )
)
def when_delete_invalid_cat_todo(invalid_todo_ID, categoryID, response):
    response["response"] = requests.delete(
        API_URL + f"/categories/{categoryID}/todos/{invalid_todo_ID}"
    )


@then(
    parsers.parse(
        "the error {error} shall be raised with http status code {httpstatus}"
    )
)
def check_delete_error(error, httpstatus, response):
    assert response["response"].status_code == int(httpstatus)
    assert response["response"].json()["errorMessages"][0] == error
