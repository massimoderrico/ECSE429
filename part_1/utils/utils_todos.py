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
empty_todos = {"todos": []}
todo_name = "Todo_1"
todo_desc = "This is a nice todo"
todo_done_status = "false"
invalid_todo_id = 0
todo_bad_field = "idd"

default_categories = {
    "categories": [
        {"id": "1", "title": "Office", "description": ""},
        {"id": "2", "title": "Home", "description": ""},
    ]
}

category_name = "Cat_1"
category_desc = "This is a nice cat"
empty_todo_categories = {"categories": []}
invalid_cat_id = 0
valid_cat_id = 2

# Error messages
no_title_err = {"errorMessages": ["title : field is mandatory"]}
post_todo_with_id = {
    "errorMessages": [
        "Invalid Creation: Failed Validation: Not allowed to create with id"
    ]
}
todo_bad_field_err = {"errorMessages": [f"Could not find field: {todo_bad_field}"]}
todo_id_not_found_id = {
    "errorMessages": [f"Could not find an instance with todos/{invalid_todo_id}"]
}
todo_id_invalid_guid = {
    "errorMessages": [f"Invalid GUID for {invalid_todo_id} entity todo"]
}
todo_id_invalid_guid_or_id = {
    "errorMessages": [
        f"No such todo entity instance with GUID or ID {invalid_todo_id} found"
    ]
}
todo_id_put_id_in_payload_err = {"errorMessages": ["Failed Validation: id should be ID"]}
todo_id_delete_err = {
    "errorMessages": [f"Could not find any instances with todos/{invalid_todo_id}"]
}
todo_invalid_id_cat_err = {
    "errorMessages": [
        f"Could not find parent thing for relationship todos/{invalid_todo_id}/categories"
    ]
}
todo_cat_with_id_err = {"errorMessages": ["Could not find thing matching value for id"]}
todo_cat_invalid_todo_id_err = {
    "errorMessages": [
        f"Could not find any instances with todos/{invalid_todo_id}/todos/{invalid_cat_id}"
    ]
}
todo_cat_invalid_todo_id_err = {
    "errorMessages": [
        f"Could not find any instances with todos/{invalid_todo_id}/todos/{invalid_cat_id}"
    ]
}
todo_invalid_id_category_err ={
    "errorMessages": [
        f"Could not find parent thing for relationship todos/{invalid_todo_id}/categories"
    ]
}

# Helper functions
def delete_todo(id):
    response = requests.delete(API_URL + f"/todos/{id}")
    assert response.status_code == 200


def create_todo(payload):
    response = requests.post(API_URL + "/todos", json=payload)
    assert response.status_code == 201
    return response.json()


def create_todo_category(todo_id, todo_payload):
    response = requests.post(API_URL + f"/todos/{todo_id}/categories", json=todo_payload)
    assert response.status_code == 201
    return response.json()


def delete_todo_category(todo_id, cat_id):
    response = requests.delete(API_URL + f"/todos/{todo_id}/categories/{cat_id}")
    assert response.status_code == 200

def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200
