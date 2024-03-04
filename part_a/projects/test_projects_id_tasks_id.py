import requests
from utils.utils import *
from utils.projects_utils import *

#options
def test_options_projects_id_tasks_id():
    response = requests.options(API_URL + "/projects/1/tasks/1")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"

#head
def test_head_projects_id_tasks_id():
    response = requests.head(API_URL + "/projects/1/tasks/1")
    assert response.status_code == 404

#delete
def test_delete_projects_id_tasks_id_bad_id():
    response = requests.delete(API_URL + "/projects/1/tasks/0")
    assert response.status_code == 404
    assert response.json() == {"errorMessages": ["Could not find any instances with projects/1/tasks/0"]}

def test_delete_projects_id_tasks_id():
    response = requests.post(API_URL + "/projects/1/tasks", json={"title": "pa qui officia deser","doneStatus": False,"description": "ex ea commodo consea"})
    id = response.json()["id"]
    response = requests.delete(API_URL + "/projects/1/tasks/" + str(id))
    assert response.status_code == 200
    response = requests.get(API_URL + "/projects/1/tasks")
    assert response.status_code == 200
    sorted_todos = sorted(response.json()["todos"], key=lambda x: x["id"])
    assert sorted_todos == sorted(default_project_tasks["todos"], key=lambda x: x["id"])
    delete_task(id)