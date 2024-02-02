import requests
from utils.utils import *
from utils.projects_utils import *


#options
def test_options_projects_id():
    response = requests.options(API_URL + "/projects/" + str(default_project_id))
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST, PUT, DELETE"

#head
def test_head_projects_id():
    response = requests.head(API_URL + "/projects/" + str(default_project_id))
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""

#get
def test_get_projects_by_id():
    response = requests.get(API_URL + "/projects/" + str(default_project_id))
    assert response.status_code == 200
    assert response.json() == {"projects": [default_projects["projects"][0]]}
    
def test_get_projects_by_invalid_id():
    response = requests.get(API_URL + "/projects/0")
    assert response.status_code == 404
    assert response.json() == get_project_bad_id

#put - Unstable, deletes other attributes
def test_put_projects_only_description():
    response = requests.put(API_URL + "/projects/" + str(default_project_id), json={"description": "This is a nice project"})
    assert response.status_code == 200
    assert response.json()["title"] == ""
    assert response.json()["description"] == "This is a nice project"
    reset_default_project()

    
def test_put_projects_only_title():
    response = requests.put(API_URL + "/projects/" + str(default_project_id), json={"title": "School Work"})
    assert response.status_code == 200
    assert response.json()["title"] == "School Work"
    assert response.json()["description"] == ""
    reset_default_project()

def test_put_projects_title_and_description():
    response = requests.put(API_URL + "/projects/" + str(default_project_id), json={"title": "School Work", "description": "This is a nice project"})
    assert response.status_code == 200
    assert response.json()["title"] == "School Work"
    assert response.json()["description"] == "This is a nice project"
    reset_default_project()

def test_put_project_bad_field():
    response = requests.put(API_URL + "/projects/" + str(default_project_id), json={"badfield": "School Work"})
    assert response.status_code == 400
    assert response.json() == post_project_bad_field

def test_put_project_bad_id():
    response = requests.put(API_URL + "/projects/0", json={"title": "School Work"})
    assert response.status_code == 404
    assert response.json() == post_project_bad_id_put

    
#post
def test_post_projects_only_description():
    response = requests.post(API_URL + "/projects/" + str(default_project_id), json={"description": "This is a nice project"})
    assert response.status_code == 200
    assert response.json()["description"] == "This is a nice project"
    reset_default_project()

def test_post_projects_only_title():
    response = requests.post(API_URL + "/projects/" + str(default_project_id), json={"title": "School Work"})
    assert response.status_code == 200
    assert response.json()["title"] == "School Work"
    reset_default_project()

def test_post_projects_title_and_description():
    response = requests.post(API_URL + "/projects/" + str(default_project_id), json={"title": "School Work", "description": "This is a nice project"})
    assert response.status_code == 200
    assert response.json()["title"] == "School Work"
    assert response.json()["description"] == "This is a nice project"
    reset_default_project()

def test_post_project_bad_field():
    response = requests.post(API_URL + "/projects/" + str(default_project_id), json={"badfield": "School Work"})
    assert response.status_code == 400
    assert response.json() == post_project_bad_field

def test_post_project_bad_id():
    response = requests.post(API_URL + "/projects/0", json={"title": "School Work"})
    assert response.status_code == 404
    assert response.json() == post_project_bad_id_post

#delete
def test_delete_project_id():
    # Create a new project
    response = requests.post(API_URL + "/projects", json={"title": "New Project", "description": "This is a new project"})
    assert response.status_code == 201
    new_project_id = response.json()["id"]

    # Delete the new project
    response = requests.delete(API_URL + "/projects/" + str(new_project_id))
    assert response.status_code == 200

    # Verify that the new project is deleted
    response = requests.get(API_URL + "/projects/" + str(new_project_id))
    assert response.status_code == 404
    assert response.json() == {
    "errorMessages": [
        "Could not find an instance with projects/" + str(new_project_id)
    ]
}

def test_delete_project_bad_id():
    response = requests.delete(API_URL + "/projects/0")
    assert response.status_code == 404
    assert response.json() == {
    "errorMessages": [
        "Could not find any instances with projects/0"
    ]
}
    