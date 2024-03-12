import requests
from utils.utils_todos import *


def test_options_todo_id_categories_id():
    response = requests.options(API_URL + "/todos/:id/categories/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


# No matter the bad id, same response
def test_delete_todo_id_categories_id_invalid_id():
    response = requests.delete(
        API_URL + f"/todos/{invalid_todo_id}/categories/{invalid_cat_id}"
    )
    assert response.status_code == 404
    assert response.json() == todo_cat_invalid_todo_id_err


def test_delete_todo_id_categories_id_valid():
    category_id = create_todo_category(
        valid_todo_id, {"title": category_name, "description": category_desc}
    ).get("id")
    response = requests.delete(API_URL + f"/todos/{valid_todo_id}/categories/{category_id}")
    assert response.status_code == 200
    assert response.text == ""
    delete_category(category_id)
