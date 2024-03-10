import pytest
from pytest_bdd import given, scenarios, then, when, parsers
from utils.cat_utils import *

scenarios("../resources/modify_category.feature")


@when(
    parsers.parse(
        "the user requests to modify the description of category {id} to description {description}"
    )
)
def when_modify_category_object_desc(id, description, response):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={"description": description},
    )


@then(
    parsers.parse(
        "the user will receive the modified category object with id {id}, title {title}, and description {description}"
    )
)
def check_all_categories(id, title, description, response):
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
def when_modify_category_object_title(id, title, response):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={"title": title},
    )


@when(parsers.parse("the user requests to modify a category with invalid id {id}"))
def when_modify_invalid_id(id, response):
    response["response"] = requests.post(
        API_URL + "/categories/" + str(id),
        json={},
    )
