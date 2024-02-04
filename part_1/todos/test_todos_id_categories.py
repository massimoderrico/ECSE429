import requests
from utils.utils_todos import *


def test_options_todos_id_categories():
    response = requests.options(API_URL + "/todos/:id/categories")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_todos_id_categories():
    response = requests.head(API_URL + f"/todos/{valid_todo_id}/categories")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get categories by todo id

################################################################ need to return all cats when invid, change return object
def test_get_todos_id_categories_invalid_todo_id():
    response = requests.get(API_URL + f"/todos/{invalid_todo_id}/categories")
    assert response.status_code == 200
    assert response.json() == {"categories": [default_categories["categories"][0]]}


def test_get_todos_id_categories_valid_todo_id():
    todo_id = 2
    response = requests.get(API_URL + f"/todos/{todo_id}/categories")
    assert response.status_code == 200
    assert response.json() == empty_todo_categories

# Test post categories by todo id


def test_post_todos_id_categories_invalid_todo_id():
    response = requests.post(API_URL + "/todos/" + str(invalid_todo_id) + "/categories")
    assert response.status_code == 404
    assert response.json() == todo_invalid_id_category_err


def test_post_todos_id_categories_no_title():
    response = requests.post(API_URL + f"/todos/{valid_todo_id}/categories", json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_post_todos_id_categories_valid_payload():
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/categories",
        json={"title": category_name, "description": category_desc}
    )
    assert response.status_code == 201
    category_id = response.json().get("id")
    assert response.json() == {
        "id": category_id,
        "title": category_name,
        "description": category_desc
    }
    delete_todo_category(valid_todo_id, category_id)
    delete_category(category_id)


def test_post_todos_id_categories_invalid_id_in_payload():
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/categories",
        json={"id": invalid_cat_id, "title": category_name, "description": category_desc},
    )
    assert response.status_code == 404
    assert response.json() == cannot_find_id_err

def test_post_todos_id_categories_valid_id_in_payload():
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/categories",
        json={"id": str(valid_cat_id)}
    )
    assert response.status_code == 201
    assert response.text == ""
    delete_todo_category(valid_todo_id, valid_cat_id)

