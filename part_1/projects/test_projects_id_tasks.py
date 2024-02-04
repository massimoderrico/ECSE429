import requests
from utils.utils import *
from utils.projects_utils import *

#options
def test_options_projects_id_tasks():
    response = requests.options(API_URL + "/projects/1/tasks")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"

#head
def test_head_projects_id_tasks():
    response = requests.head(API_URL + "/projects/1/tasks")
    assert response.status_code == 200

#get
def test_get_projects_id_tasks_by_valid_id():
    response = requests.get(API_URL + "/projects/1/tasks")
    assert response.status_code == 200
    sorted_todos = sorted(response.json()["todos"], key=lambda x: x["id"])
    assert sorted_todos == sorted(default_project_tasks["todos"], key=lambda x: x["id"])

# def test_get_projects_id_tasks_by_invalid_id():
#     response = requests.get(API_URL + "/projects/0/tasks")
#     assert response.status_code == 404
#     assert response.json() == get_project_bad_id
    
def test_get_projects_id_tasks_by_invalid_param_value():
    response = requests.get(API_URL + "/projects/1/tasks", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_todos

def test_get_projects_id_tasks_by_valid_title_param():
    response = requests.get(API_URL + "/projects/1/tasks", params={"title": "scan paperwork"})
    assert response.status_code == 200
    assert response.json() == {"todos":[default_project_tasks["todos"][1]]}

def test_get_projects_id_tasks_by_valid_description_param():
    response = requests.get(API_URL + "/projects/1/tasks", params={"description": ""})
    sorted_todos = sorted(response.json()["todos"], key=lambda x: x["id"])
    assert sorted_todos == sorted(default_project_tasks["todos"], key=lambda x: x["id"])


def test_get_projects_id_tasks_by_invalid_param():
    response = requests.get(API_URL + "/projects/1/tasks", params={"bad_key": "0"})
    sorted_todos = sorted(response.json()["todos"], key=lambda x: x["id"])
    assert sorted_todos == sorted(default_project_tasks["todos"], key=lambda x: x["id"])


#post
def test_post_projects_id_tasks():
    response = requests.post(API_URL + "/projects/1/tasks", json={"title": "pa qui officia deser","doneStatus": False,"description": "ex ea commodo consea"})
    assert response.status_code == 201
    delete_project_task(response.json()["id"])

def test_post_projects_id_tasks_no_title():
    response = requests.post(API_URL + "/projects/1/tasks", json={"doneStatus": False,"description": "ex ea commodo consea"})
    assert response.status_code == 400
    assert response.json() == post_project_no_title

def test_post_projects_id_tasks_no_doneStatus():
    response = requests.post(API_URL + "/projects/1/tasks", json={"title": "pa qui officia deser","description": "ex ea commodo consea"})
    assert response.status_code == 201
    delete_project_task(response.json()["id"])

def test_post_projects_id_tasks_no_description():
    response = requests.post(API_URL + "/projects/1/tasks", json={"title": "pa qui officia deser","doneStatus": False})
    assert response.status_code == 201
    delete_project_task(response.json()["id"])
