import pytest
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.cat_utils import *


@scenario(
    "../resources/categories/delete_cat_relationships.feature",
    "Delete a category todo",
)
def test_delete_cat_relationships_normal():
    pass


@scenario(
    "../resources/categories/delete_cat_relationships.feature",
    "Delete a category project",
)
def test_delete_cat_relationships_alternative():
    pass


@scenario(
    "../resources/categories/delete_cat_relationships.feature",
    "Delete a category todo with invalid category todo ID",
)
def test_delete_cat_relationships_error():
    pass


@given(
    parsers.parse(
        "the database contains the category todo with title {title}, done status {doneStatus}, and description {description} under category {categoryID}"
    )
)
def create_cat_todo(
    title, description, doneStatus, categoryID, cat_todos, reset_database_cats
):
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
def create_cat_project(
    title, description, categoryID, cat_projects, reset_database_cats
):
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
def when_delete_cat_todo(categoryID, cat_todos, response, reset_database_cats):
    todo_id = cat_todos["cat_todos"][0]["id"]
    response["response"] = requests.delete(
        API_URL + f"/categories/{categoryID}/todos/{todo_id}"
    )
    # Double delete
    response = requests.delete(API_URL + f"/todos/{todo_id}")
    assert response.status_code == 200


@then(
    parsers.parse("the status code {status_code} will be received with the text {text}")
)
def check_status_code_and_text(status_code, text, response, reset_database_cats):
    assert response["response"].status_code == int(status_code)
    assert response["response"].text == text.replace('"', "")


@when(
    parsers.parse("the user requests to delete the project under category {categoryID}")
)
def when_delete_cat_project(categoryID, cat_projects, response, reset_database_cats):
    project_id = cat_projects["cat_projects"][0]["id"]
    response["response"] = requests.delete(
        API_URL
        + f"/categories/{categoryID}/projects/{cat_projects['cat_projects'][0]['id']}"
    )
    # Double delete
    response = requests.delete(API_URL + f"/projects/{project_id}")
    assert response.status_code == 200


@when(
    parsers.parse(
        "the user requests to delete the todo with invalid ID {invalid_todo_ID} under the category {categoryID}"
    )
)
def when_delete_invalid_cat_todo(
    invalid_todo_ID, categoryID, response, reset_database_cats
):
    response["response"] = requests.delete(
        API_URL + f"/categories/{categoryID}/todos/{invalid_todo_ID}"
    )


@then(
    parsers.parse(
        "the error {error} shall be raised with http status code {httpstatus}"
    )
)
def check_delete_error(error, httpstatus, response, reset_database_cats):
    assert response["response"].status_code == int(httpstatus)
    assert response["response"].json()["errorMessages"][0] == error
