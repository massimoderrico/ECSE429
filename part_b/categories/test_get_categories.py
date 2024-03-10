import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from utils.cat_utils import *


scenarios("../resources/get_categories.feature")


@when("the user requests to get all categories")
def all_categories_resp(response):
    response["response"] = requests.get(API_URL + "/categories")


@then("the user will receive a list of all categories")
def check_all_categories(todos, response):
    assert {
        "categories": sorted(
            response["response"].json()["categories"], key=lambda x: int(x["id"])
        )
    } == todos


@when(parsers.parse("the user requests to get all categories with title {title}"))
def get_all_categories_with_title(title, response):
    response["response"] = requests.get(
        API_URL + "/categories", params={"title": title}
    )


@then(
    parsers.parse("the user will receive a list of all categories with title {title}")
)
def check_all_cat_with_desc(todos, title, response):
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
def get_all_categories_invalid_id(id, response):
    response["response"] = requests.get(API_URL + "/categories", params={"id": id})


@then("the user will receive an empty list of categories")
def check_empty_cat(response):
    assert response["response"].json() == empty_categories
