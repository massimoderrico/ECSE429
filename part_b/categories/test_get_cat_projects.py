import pytest
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.cat_utils import *


@scenario(
    "../resources/categories/get_cat_projects.feature",
    "Get all projects under a category",
)
def test_get_cat_projects_normal():
    pass


@scenario(
    "../resources/categories/get_cat_projects.feature",
    "Get no project under a category",
)
def test_get_cat_projects_alternative():
    pass


@scenario(
    "../resources/categories/get_cat_projects.feature",
    "Get all projects under invalid category",
)
def test_get_cat_projects_error():
    pass


@given(
    parsers.parse(
        "the database contains a category project with title {title}, description {description}, completed status {completed}, and active status {active} under category {categoryID}"
    )
)
def create_cat_project(
    title, description, completed, active, categoryID, cat_projects, reset_database_cats
):
    params = {
        "title": title,
        "description": description,
        "completed": True if completed.lower() == "true" else False,
        "active": True if active.lower() == "true" else False,
    }
    response = requests.post(
        API_URL + f"/categories/{categoryID}/projects", json=params
    )
    assert response.status_code == 201
    cat_projects["cat_projects"].append(response.json())


@when(
    parsers.parse("the user requests to get all projects under category {categoryID}")
)
def get_all_projects_under_cat(categoryID, response, reset_database_cats):
    response["response"] = requests.get(API_URL + f"/categories/{categoryID}/projects")


@then(
    parsers.parse(
        "the user will receive a list of all projects under category {categoryID}"
    )
)
def check_projects_under_cat(categoryID, response, cat_projects, reset_database_cats):
    assert sorted(cat_projects["cat_projects"], key=lambda x: int(x["id"])) == sorted(
        response["response"].json()["projects"], key=lambda x: int(x["id"])
    )


@then("the user will receive an empty list of projects")
def check_no_project_under_cat(response, reset_database_cats):
    assert response["response"].json()["projects"] == []


@then("the user will receive all projects under all categories")
def check_projects_under_all_cat(response, cat_projects, reset_database_cats):
    assert sorted(cat_projects["cat_projects"], key=lambda x: int(x["id"])) == sorted(
        response["response"].json()["projects"], key=lambda x: int(x["id"])
    )
