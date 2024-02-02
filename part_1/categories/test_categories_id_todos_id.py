import requests
from utils.utils import *


def test_options_cat_id_todos_id():
    response = requests.options(API_URL + "/categories/:id/todos/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


# No matter the bad id, same response
def test_delete_cat_id_todos_id_invalid_id():
    response = requests.delete(
        API_URL + f"/categories/{invalid_cat_id}/todos/{invalid_todo_id}"
    )
    assert response.status_code == 404
    assert response.json() == cat_todo_invalid_cat_id_err


def test_delete_cat_id_todos_id_valid():
    cat_id = 1
    todo_id = create_cat_todo(
        cat_id, {"title": todo_name, "description": todo_desc}
    ).get("id")
    response = requests.delete(API_URL + f"/categories/{cat_id}/todos/{todo_id}")
    assert response.status_code == 200
    assert response.text == ""
