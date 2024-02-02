import requests
from utils.utils import *


def test_options_cat_id_todos():
    response = requests.options(API_URL + "/categories/:id/todos")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_cat_id_todos():
    response = requests.head(API_URL + "/categories/1/todos")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get todos by category id


def test_get_cat_id_todos_invalid_cat_id():
    cat_id = 1
    # Create under a good category
    todo = create_cat_todo(cat_id, {"title": todo_name, "description": todo_desc})
    response = requests.get(API_URL + f"/categories/{invalid_cat_id}/todos")
    assert response.status_code == 200
    assert response.json() == {"todos": [todo]}
    delete_cat_todo(cat_id, todo.get("id"))


def test_get_cat_id_todos_valid_cat_id_empty():
    cat_id = 1
    response = requests.get(API_URL + f"/categories/{cat_id}/todos")
    assert response.status_code == 200
    assert response.json() == empty_cat_todos


def test_get_cat_id_todos_for_one_cat_id():
    cat_id = 1
    other_cat_id = 2
    todo = create_cat_todo(cat_id, {"title": todo_name, "description": todo_desc})
    response = requests.get(API_URL + f"/categories/{other_cat_id}/todos")
    assert response.status_code == 200
    assert response.json() == empty_cat_todos
    delete_cat_todo(cat_id, todo.get("id"))


# Test post todos by category id


def test_post_cat_id_todos_invalid_cat_id():
    response = requests.post(API_URL + "/categories/" + str(invalid_cat_id) + "/todos")
    assert response.status_code == 404
    assert response.json() == cat_invalid_id_todo_err


def test_post_cat_id_todos_no_title():
    cat_id = 1
    response = requests.post(API_URL + f"/categories/{cat_id}/todos", json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_post_cat_id_todos_valid_payload():
    cat_id = 1
    response = requests.post(
        API_URL + f"/categories/{cat_id}/todos",
        json={"title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 201
    todo_id = response.json().get("id")
    assert response.json() == {
        "id": todo_id,
        "title": todo_name,
        "doneStatus": "false",
        "description": todo_desc,
    }
    delete_cat_todo(cat_id, todo_id)


def test_post_cat_id_todos_id_in_payload():
    cat_id = 1
    response = requests.post(
        API_URL + f"/categories/{cat_id}/todos",
        json={"id": 1, "title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 404
    assert response.json() == cat_todo_with_id_err
