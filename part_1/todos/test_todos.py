import requests
from utils.utils_todos import *


def test_options_todos():
    response = requests.options(API_URL + "/todos")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_todos():
    response = requests.head(API_URL + "/todos")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get todos
def test_get_todos_no_params():
    response = requests.get(API_URL + "/todos")
    assert response.status_code == 200
    assert {
        "todos": sorted(response.json()["todos"], key=lambda x: int(x["id"]))
    } == default_todos


def test_get_todos_by_valid_id():
    response = requests.get(API_URL + "/todos", params={"id": str(valid_todo_id)})
    assert response.status_code == 200
    assert response.json() == {"todos": [default_todos["todos"][valid_todo_id-1]]}


def test_get_todos_by_valid_title():
    response = requests.get(API_URL + "/todos", params={"title": "scan paperwork"})
    assert response.status_code == 200
    assert response.json() == {"todos": [default_todos["todos"][valid_todo_id-1]]}


def test_get_todos_by_valid_description():
    response = requests.get(API_URL + "/todos", params={"description": ""})
    assert response.status_code == 200
    assert {
        "todos": sorted(response.json()["todos"], key=lambda x: int(x["id"]))
    } == default_todos


def test_get_todos_by_invalid_param_value():
    response = requests.get(API_URL + "/todos", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_todos


def test_get_todos_by_inexistent_param():
    response = requests.get(API_URL + "/todos", params={"bad_key": "0"})
    assert response.status_code == 200
    assert {
        "todos": sorted(response.json()["todos"], key=lambda x: int(x["id"]))
    } == default_todos


# Test post todos


def test_post_todo_no_title():
    response = requests.post(API_URL + "/todos", json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_post_todo_only_title():
    response = requests.post(API_URL + "/todos", json={"title": todo_name})
    assert response.status_code == 201
    delete_todo(response.json()["id"])
    assert response.json()["title"] == todo_name


def test_post_todo_with_title_and_id():
    response = requests.post(
        API_URL + "/todos", json={"id": "0", "title": todo_name}
    )
    assert response.status_code == 400
    assert response.json() == post_todo_with_id


def test_post_todo_with_title_desc():
    response = requests.post(
        API_URL + "/todos",
        json={"title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 201
    todo_id = response.json().get("id")
    assert response.json() == {
        "id": todo_id,
        "title": todo_name,
        "doneStatus": todo_done_status,
        "description": todo_desc
    }
    delete_todo(todo_id)


def test_post_todo_with_bad_field():
    response = requests.post(
        API_URL + "/todos", json={ todo_bad_field : "0", "title": todo_name}
    )
    assert response.status_code == 400
    assert response.json() == todo_bad_field_err
