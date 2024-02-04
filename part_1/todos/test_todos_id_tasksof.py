import requests
from utils.utils_todos import *


def test_options_todos_id_tasksof():
    response = requests.options(API_URL + "/todos/:id/tasksof")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_todos_id_tasksof():
    response = requests.head(API_URL + "/todos/1/tasksof")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get tasksof by todo id

################################################################ need to return all taskofs when invid, change return object
# def test_get_todos_id_tasksof_invalid_todo_id():
#     taskof_id = 0
#     # Create under a good todo
#     response = requests.get(API_URL + f"/todos/{invalid_todo_id}/tasksof")
#     assert response.status_code == 200
#     assert response.json() == {"tasksof": [default_tasksof["tasksof"][taskof_id]]}


def test_get_todos_id_tasksof_valid_todo_id():
    response = requests.get(API_URL + f"/todos/{valid_todo_id}/tasksof")
    assert response.status_code == 200
    assert response.json() == default_tasksof
# # Test post tasksof by todo id

def test_post_todos_id_tasksof_invalid_todo_id():
    response = requests.post(API_URL + "/todos/" + str(invalid_todo_id) + "/tasksof")
    assert response.status_code == 404
    assert response.json() == todo_invalid_id_taskof_err

def test_post_todos_id_tasksof_no_title():
    response = requests.post(API_URL + f"/todos/{valid_todo_id}/tasksof", json={})
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert response.json() == {
        "id": project_id,
        "title": "",
        "description": "",
        "completed": taskof_completed,
        "active": taskof_active,
        'tasks': [{'id': str(valid_todo_id)}],
    }
    delete_project(project_id)

def test_post_todos_id_tasksof_with_title():
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/tasksof",
        json={"title": taskof_name, "description": taskof_desc}
    )
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert response.json() == {
        "id": project_id,
        "title": taskof_name,
        "description": taskof_desc,
        "completed": taskof_completed,
        "active": taskof_active,
        'tasks': [{'id': str(valid_todo_id)}],
    }
    delete_project(project_id)


def test_post_todos_id_tasksof_invalid_id_in_payload():
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/tasksof",
        json={"id": invalid_taskof_id, "title": taskof_name, "description": taskof_desc},
    )
    assert response.status_code == 404
    assert response.json() == cannot_find_id_err

def test_post_todos_id_tasksof_valid_id_in_payload():
    project_id = create_project({}).get("id")
    response = requests.post(
        API_URL + f"/todos/{valid_todo_id}/tasksof",
        json={"id": str(project_id)}
    )
    assert response.status_code == 201
    assert response.text == ""
    delete_project(project_id)

