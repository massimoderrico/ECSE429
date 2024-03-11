import pytest
from pytest_bdd import given, scenario, then, when, parsers
from utils_b.cat_utils import *


@scenario(
    "../resources/categories/modify_category.feature",
    "Modify the description of a category",
)
def test_modify_category_normal():
    pass


@scenario(
    "../resources/categories/modify_category.feature",
    "Modify the title of a category",
)
def test_modify_category_alternative():
    pass


@scenario(
    "../resources/categories/modify_category.feature",
    "Modify a category with an invalid category ID",
)
def test_modify_category_error():
    pass


@when(
    parsers.parse(
        "the user requests to modify the description of category {id} to description {description}"
    )
)
def when_modify_category_object_desc(id, description, response, reset_database_cats):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={"description": description},
    )


@then(
    parsers.parse(
        "the user will receive the modified category object with id {id}, title {title}, and description {description}"
    )
)
def check_all_categories(id, title, description, response, reset_database_cats):
    todo = response["response"].json()
    assert todo["id"] == id
    assert todo["title"] == title
    # Need to remove "" since no empty string symbol
    assert todo["description"] == description.replace('"', "")


@when(
    parsers.parse(
        "the user requests to modify the description of category {id} to title {title}"
    )
)
def when_modify_category_object_title(id, title, response, reset_database_cats):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={"title": title},
    )


@when(parsers.parse("the user requests to modify a category with invalid id {id}"))
def when_modify_invalid_id(id, response, reset_database_cats):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={},
    )
