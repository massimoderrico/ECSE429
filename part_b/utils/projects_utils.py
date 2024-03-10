import requests
from utils.utils import *

#defaults
default_projects = {
    "projects": [
        {"id": "1", "title": "Office Work", "completed": 'false', "active": 'false', "description": "", "tasks": [{"id": "1"},{"id": "2"}]}
    ]
}

default_project = {"id": "1", "title": "Office Work", "completed": 'false', "active": 'false', "description": "", "tasks": [{"id": "2"},{"id": "1"}]}

default_projects_no_id = {
    "projects": [
        {"title": "Office Work", "completed": 'false', "active": 'false', "description": "", "tasks": [{"id": "1"},{"id": "2"}]}
    ]
}
empty_projects = {"projects": []}

empty_todos = {"todos": []}

default_project_id = 1

default_project_category = {"title": "Office", "description": "Office Description"}

default_project_tasks = {"todos":[{"id":"2","title":"file paperwork","doneStatus":"false","description":"","tasksof":[{"id":"1"}]},{"id":"1","title":"scan paperwork","doneStatus":"false","description":"","categories":[{"id":"1"}],"tasksof":[{"id":"1"}]}]}



#error messages
post_category_no_title = {"errorMessages": ["title : field is mandatory"]}
post_category_bad_field = {"errorMessages": ["Could not find field: idd"]}

category_name = "Cat_1"
category_desc = "This is a nice cat"

post_project_no_title = {"errorMessages": ["title : field is mandatory"]}
post_project_with_id = {
    "errorMessages": [
        "Invalid Creation: Failed Validation: Not allowed to create with id"
    ]
}
post_project_bad_field = {"errorMessages": ["Could not find field: badfield"]}
get_project_bad_id = {
    "errorMessages": [
        "Could not find an instance with projects/0"
    ]
}
post_project_bad_id_put = {
    "errorMessages": [
        "Invalid GUID for 0 entity project"
    ]
}
post_project_bad_id_post = {
    "errorMessages": [
        "No such project entity instance with GUID or ID 0 found"
    ]
}

post_task_no_donestatus = {"errorMessages": ["doneStatus : field is mandatory"]}

post_task_no_description = {"errorMessages": ["description : field is mandatory"]}

#helper functions
def delete_project(id):
    response = requests.delete(API_URL + f"/projects/{id}")
    assert response.status_code == 200

def reset_default_project_description():
    response = requests.post(API_URL + "/projects/1", json={"description": ""})
    assert response.status_code == 200

def reset_default_project_title():
    response = requests.post(API_URL + "/projects/1", json={"title": "Office Work"})
    assert response.status_code == 200

def reset_default_project_tasks():
    response = requests.post(API_URL + "/projects/1", json={"tasks": [{"id": "1"},{"id": "2"}]})
    assert response.status_code == 200

def reset_default_project():
    reset_default_project_description()
    reset_default_project_title()
    reset_default_project_tasks()

def create_default_project_category():
    response = requests.post(API_URL + "/projects/1/categories", json=default_project_category)
    assert response.status_code == 201
    return int(response.json()["id"])
    
def delete_default_project_category(id):
    response = requests.delete(API_URL + "/projects/1/categories/" + str(id))
    assert response.status_code == 200

def delete_category(id):
    response = requests.delete(API_URL + "/categories/" + str(id))
    assert response.status_code == 200
    
def delete_project_task(id):
    response = requests.delete(API_URL + "/projects/1/tasks/" + str(id))
    assert response.status_code == 200

def delete_task(id):
    response = requests.delete(API_URL + "/todos/" + str(id))
    assert response.status_code == 200  

def create_project(title, description):
    response = requests.post(API_URL + "/projects", json={"title": title, "description": description})
    print(response.status_code)
    assert response.status_code == 201

    return int(response.json()["id"])

def delete_todo_and_relationship(todo_title, project_id):
    response = requests.get(API_URL + "/projects/" + str(project_id) + "/tasks")
    todos = response.json()["todos"]
    for todo in todos:
        if todo["title"] == todo_title:
            delete_task(todo["id"])
            response = requests.get(API_URL + "/projects/" + str(project_id) + "/tasks")
            todos = response.json()["todos"]
            for todo in todos:
                if todo["title"] == todo_title:
                    delete_project_task(todo["id"])
                    break
            break
    