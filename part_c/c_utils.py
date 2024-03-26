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

default_categories = {
    "categories": [
        { 
            "id": "1",
            "title": "Office", 
            "description": ""
        },
        {   
            "id": "2", 
            "title": "Home",
            "description": ""
        },
    ]
}

default_projects = {
    "projects": [
        {
            "id": "1", 
            "title": "Office Work", 
            "completed": 'false', 
            "active": 'false', "description": "", 
            "tasks": [
                {
                    "id": "1"
                },
                {
                    "id": "2"
                }
            ]
        }
    ]
}

# Todo dummy data
todo_payload = {
            "title": "Todo_1",
            "description": "This is a nice todo"
        }
todo_modified_payload = {
            "title": "Modified_Todo_1",
            "description": "This is not a nice modifed todo"
        }

# Project dummy data
project_payload = {
            "title": "Project_1",
            "description": "This is a nice project"
        }
project_modified_payload = {
            "title": "Modified_Project_1",
            "description": "This is not a nice modifed project"
        }

# Category dummy data
category_payload = {
            "title": "Category_1",
            "description": "This is a nice category"
        }
category_modified_payload = {
            "title": "Modified_Category_1",
            "description": "This is not a nice modifed category"
        }

# Todo helper functions
def get_todos():
    response = requests.get(API_URL + "/todos")
    assert response.status_code == 200
    return response.json()

def create_todo(payload):
    response = requests.post(API_URL + "/todos", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_todo(id, payload):
    response = requests.post(API_URL + f"/todos/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_todo(id):
    response = requests.delete(API_URL + f"/todos/{id}")
    assert response.status_code == 200

# Project helper functions

def create_project(payload):
    response = requests.post(API_URL + "/projects", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_project(id, payload):
    response = requests.post(API_URL + f"/projects/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_project(id):
    response = requests.delete(API_URL + f"/projects/{id}")
    assert response.status_code == 200

# Category helper functions
    
def create_category(payload):
    response = requests.post(API_URL + "/categories", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_category(id, payload):
    response = requests.post(API_URL + f"/categories/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200



    