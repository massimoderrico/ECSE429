import requests
from utils.utils_todos import *


def test_options_todo_id_tasksof_id():
    response = requests.options(API_URL + "/todos/:id/tasksof/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


# No matter the bad id, same response
def test_delete_todo_id_tasksof_id_invalid_id():
    response = requests.delete(
        API_URL + f"/todos/{invalid_todo_id}/tasksof/{invalid_taskof_id}"
    )
    assert response.status_code == 404
    assert response.json() == todo_taskof_invalid_todo_id_err


def test_delete_todo_id_taskof_id_valid():
    taskof_id = create_todo_taskof(
        valid_todo_id, {"title": taskof_name, "description": taskof_desc}
    ).get("id")
    response = requests.delete(API_URL + f"/todos/{valid_todo_id}/tasksof/{taskof_id}")
    assert response.status_code == 200
    assert response.text == ""
    delete_project(taskof_id)