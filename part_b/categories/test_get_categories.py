import pytest
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.cat_utils import *


@scenario(
    "../resources/categories/get_categories.feature",
    "Get all categories",
)
def test_get_categories_normal():
    pass


@scenario(
    "../resources/categories/get_categories.feature",
    "Get all categories matching a title",
)
def test_get_categories_alternative():
    pass


@scenario(
    "../resources/categories/get_categories.feature",
    "Get all categories matching an invalid category ID",
)
def test_get_categories_error():
    pass


@when("the user requests to get all categories")
def all_categories_resp(response, reset_database_cats):
    response["response"] = requests.get(API_URL + "/categories")


@then("the user will receive a list of all categories")
def check_all_categories(todos, response, reset_database_cats):
    assert {
        "categories": sorted(
            response["response"].json()["categories"], key=lambda x: int(x["id"])
        )
    } == todos


@when(parsers.parse("the user requests to get all categories with title {title}"))
def get_all_categories_with_title(title, response, reset_database_cats):
    response["response"] = requests.get(
        API_URL + "/categories", params={"title": title}
    )


@then(
    parsers.parse("the user will receive a list of all categories with title {title}")
)
def check_all_cat_with_desc(todos, title, response, reset_database_cats):
    filtered_response = list(
        filter(
            lambda category: category["title"] == title,
            response["response"].json()["categories"],
        )
    )
    filtered_todos = list(
        filter(lambda category: category["title"] == title, todos["categories"])
    )
    assert sorted(filtered_response, key=lambda x: int(x["id"])) == filtered_todos


@when(parsers.parse("the user requests to get all categories with invalid id {id}"))
def get_all_categories_invalid_id(id, response, reset_database_cats):
    response["response"] = requests.get(API_URL + "/categories", params={"id": id})


@then("the user will receive an empty list of categories")
def check_empty_cat(response, reset_database_cats):
    assert response["response"].json() == empty_categories
