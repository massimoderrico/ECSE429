import requests
from utils.utils import *
from utils.projects_utils import *


#options
def test_options_projects_id_categories():
    response = requests.options(API_URL + "/projects/1/categories")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"

#head
def test_head_projects_id_categories():
    response = requests.head(API_URL + "/projects/1/categories")
    assert response.status_code == 200

#get
def test_get_projects_id_categories_by_valid_id():
    create_default_project_category()
    response = requests.get(API_URL + "/projects/1/categories")
    assert response.status_code == 200
    
    data = response.json()['categories'][0]
    
    data_without_id = {key: value for key, value in data.items() if key != "id"}
    
    assert data_without_id == default_project_category
    delete_default_project_category(data['id'])
    delete_category(data["id"])

def test_get_projects_id_categories_by_invalid_param_value():
    response = requests.get(API_URL + "/projects/1/categories", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_categories

def test_get_projects_id_categories_valid_title_param():
    create_default_project_category()
    response = requests.get(API_URL + "/projects/1/categories", params={"title": "Office"})
    assert response.status_code == 200
    data = response.json()['categories'][0]
    
    data_without_id = {key: value for key, value in data.items() if key != "id"}
    
    assert data_without_id == default_project_category
    delete_default_project_category(data['id'])
    delete_category(data["id"])

def test_get_projects_id_categories_valid_description_param():
    create_default_project_category()
    response = requests.get(API_URL + "/projects/1/categories", params={"description": "Office Description"})
    assert response.status_code == 200
    data = response.json()['categories'][0]
    
    data_without_id = {key: value for key, value in data.items() if key != "id"}
    
    assert data_without_id == default_project_category
    delete_default_project_category(data['id'])
    delete_category(data["id"])



def test_get_projects_id_categories_by_invalid_param():
    response = requests.get(API_URL + "/projects/1/categories", params={"bad_key": "0"})
    assert response.status_code == 200
    assert response.json() == empty_categories

#post
def test_post_projects_id_categories_no_title():
    response = requests.post(API_URL + "/projects/1/categories", json={"description": "This is a nice cat"})
    assert response.status_code == 400
    assert response.json() == post_category_no_title

def test_post_projects_id_categories_with_id():
    response = requests.post(API_URL + "/projects/1/categories", json={"id": "0", "title": "Office Category", "description": "Office Description"})
    assert response.status_code == 404
    assert response.json() == {
    "errorMessages": [
        "Could not find thing matching value for id"
    ]
}

def test_post_projects_id_categories():
    response = requests.post(API_URL + "/projects/1/categories", json={"title": "Office", "description": "This is a nice cat"})
    assert response.status_code == 201
    assert response.json()["title"] == "Office"
    assert response.json()["description"] == "This is a nice cat"
    delete_default_project_category(response.json()["id"])
    delete_category(response.json()["id"])
