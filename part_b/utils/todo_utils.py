import requests

API_URL = "http://localhost:4567"

# Default data
default_todos = {
    "todos": [
        {
            "id": "1",
            "title": "scan paperwork",
            "doneStatus": "false",
            "description": "",
            "categories": [
                {
                    "id": "1"
                }
            ],
            "tasksof": [
                {
                    "id": "1"
                }
            ]
        },
        {
            "id": "2",
            "title": "file paperwork",
            "doneStatus": "false",
            "description": "",
            "tasksof": [
                {
                    "id": "1"
                }
            ]
        }
    ]
}

empty_todos = {"todos" : []}
todo_name = "Todo_1"
todo_desc = "This is a nice todo"
todo_done_status = "false"
todo_bad_field = "idd"

def reset_default_todo_values(title, description, id):
    response =  requests.post(API_URL + f"/todos/{id}", json={"title": title, "description": description})
    assert response.status_code == 200

def delete_todo(id):
    response = requests.delete(API_URL + f"/todos/{id}")
    assert response.status_code == 200

def create_todo(payload):
    response = requests.post(API_URL + "/todos", json=payload)
    assert response.status_code == 201
    return response.json()

def double_delete_todo_taskof(todo_id, taskof_id):
    response = requests.delete(API_URL + f"/todos/{todo_id}/tasksof/{taskof_id}")
    assert response.status_code == 200
    response = requests.delete(API_URL + f"/projects/{taskof_id}")
    assert response.status_code == 200