import pytest
from pytest_bdd import given, then, parsers
from utils.todo_utils import *

@pytest.fixture
def todos():
    return {"todos": []}

# @pytest.fixture
# def cat_projects():
#     return {"cat_projects": []}


# @pytest.fixture
# def cat_todos():
#     return {"cat_todos": []}


@pytest.fixture
def response():
    return {}


@given("the API is responsive")
def api_is_responsive():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"


@given("the database contains the default todo objects")
def database_contains_default_todo_objects():
    # cleanup_todos()
    response = requests.get(API_URL + "/todos")
    assert response.status_code == 200
    todos = sorted(response.json()["todos"], key=lambda x: int(x["id"]))
    assert todos == default_todos["todos"]
    # todos["todos"] = default_todos["todos"]


@then(parsers.parse("the status code {status_code} will be received"))
def check_status_code(status_code, response):
    assert response["response"].status_code == int(status_code)


@then(
    parsers.parse(
        "the error {error} shall be raised with http status code {httpstatus}"
    )
)
def modify_invalid_id_error(error, httpstatus, response):
    assert response["response"].status_code == int(httpstatus)
    assert response["response"].json()["errorMessages"][0] == error

# @pytest.hookimpl
# def pytest_bdd_after_scenario(request,feature,scenario):
#     og_todo = filter(lambda todo : todo["id"] == id ,default_todos["todos"])
    ## restore default todos, delete any other todos