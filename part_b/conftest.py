import pytest
from pytest_bdd import given, then, parsers
from utils_b.cat_utils import *
from utils_b.projects_utils import *
from utils_b.todo_utils import *


@pytest.fixture
def context():
    return {}


@pytest.fixture
def cats():
    return {"categories": []}

@pytest.fixture
def todos():
    return {"todos": []}

@pytest.fixture
def todo_cat():
    return {"todo_cat": []}

@pytest.fixture
def cat_projects():
    return {"cat_projects": []}


@pytest.fixture
def cat_todos():
    return {"cat_todos": []}


@pytest.fixture
def response():
    return {"response": {}}


@pytest.fixture()
def reset_database_cats(scope="module"):
    yield
    cleanup_cats()

@given("the API is responsive")
def api_is_responsive():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"

@given("the database contains the default todo objects")
def database_contains_default_todo_objects():
    response = requests.get(API_URL + "/todos")
    assert response.status_code == 200
    todos = sorted(response.json()["todos"], key=lambda x: int(x["id"]))
    assert todos == default_todos["todos"]

@given("the database contains the default category objects")
def database_contains_default_category_objects(cats):
    # cleanup_cats()
    response = requests.get(API_URL + "/categories")
    assert response.status_code == 200
    categories = sorted(response.json()["categories"], key=lambda x: int(x["id"]))
    assert categories == default_categories["categories"]
    cats["categories"] = default_categories["categories"]


@given("the database contains the default project objects")
def get_default_projects():
    response = requests.get(API_URL + "/projects")
    assert response.status_code == 200
    modified_response = response.json()
    for project in modified_response["projects"]:
        project["tasks"] = sorted(project["tasks"], key=lambda x: int(x["id"]))
    assert modified_response == default_projects


@then(parsers.parse("the status code {status_code} will be received"))
def check_status_code(status_code, response):
    assert response["response"].status_code == int(status_code)


@then(parsers.parse('the status code "{status_code}" will be returned'))
def check_status_code(status_code, context):
    response = context["response"]
    assert response.status_code == int(status_code)


@then(
    parsers.parse(
        "the error {error} shall be raised with http status code {httpstatus}"
    )
)
def modify_invalid_id_error(error, httpstatus, response):
    assert response["response"].status_code == int(httpstatus)
    assert response["response"].json()["errorMessages"][0] == error
