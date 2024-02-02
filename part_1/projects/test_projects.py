import requests
from utils.utils import *

#testing options
def test_options_projects():
    response = requests.options(API_URL + "/projects")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"

#testing head
def test_get_projects_no_params():
    response = requests.get(API_URL + "/projects")
    assert response.status_code == 200
    assert {
        "projects": sorted(response.json()["projects"], key=lambda x: int(x["id"]))
    } == default_projects


#testing get
def test_get_projects_by_valid_id():
    response = requests.get(API_URL + "/projects", params={"id": "1"})
    assert response.status_code == 200
    assert response.json() == {"projects": [default_projects["projects"][0]]}

def test_get_projects_by_valid_title():
    response = requests.get(API_URL + "/projects", params={"title": "Office Work"})
    assert response.status_code == 200
    assert response.json() == {"projects": [default_projects["projects"][0]]}

def test_get_projects_by_valid_description():
    response = requests.get(API_URL + "/projects", params={"description": ""})
    assert response.status_code == 200
    assert response.json() == {"projects": [default_projects["projects"][0]]}

def test_get_projects_by_invalid_param_value():
    response = requests.get(API_URL + "/projects", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_projects

def test_get_projects_by_inexistent_param():
    response = requests.get(API_URL + "/projects", params={"bad_key": "0"})
    assert response.status_code == 200
    assert {
        "projects": sorted(response.json()["projects"], key=lambda x: int(x["id"]))
    } == default_projects

#testing post
def test_post_projects_no_title():
    response = requests.post(API_URL + "/projects", json={"description": "This is a nice project"})
    assert response.status_code == 201
    delete_project(response.json()["id"])
    assert response.json()["title"] == ""
    assert response.json()["description"] == "This is a nice project"


def test_post_projects_with_id():
    response = requests.post(API_URL + "/projects", json={"id": "1", "title": "Office Work", "description": "This is a nice project"})
    assert response.status_code == 400
    assert response.json() == post_project_with_id

def test_post_projects_bad_field():
    response = requests.post(API_URL + "/projects", json={"badfield": "", "title": "Office Work", "description": "This is a nice project"})
    assert response.status_code == 400
    assert response.json() == post_project_bad_field

def test_post_projects():
    response = requests.post(API_URL + "/projects", json={"title": "Office Work", "description": "This is a nice project"})
    assert response.status_code == 201
    delete_project(response.json()["id"])
    assert response.json()["title"] == "Office Work"
    assert response.json()["description"] == "This is a nice project"
