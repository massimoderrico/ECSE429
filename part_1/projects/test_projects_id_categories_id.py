import requests
from utils.utils import *
from utils.projects_utils import *

#options
def test_options_projects_id_categories_id():
    response = requests.options(API_URL + "/projects/1/categories/1")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"

#head
def test_head_projects_id_categories_id():
    response = requests.head(API_URL + "/projects/1/categories/1")
    assert response.status_code == 404

#delete
def test_delete_projects_id_categories_id_bad_id():
    response = requests.delete(API_URL + "/projects/1/categories/0")
    assert response.status_code == 404
    assert response.json() == {"errorMessages": ["Could not find any instances with projects/1/categories/0"]}

def test_delete_projects_id_categories_id():
    id = create_default_project_category()
    response = requests.delete(API_URL + "/projects/1/categories/" + str(id))
    assert response.status_code == 200
    response = requests.get(API_URL + "/projects/1/categories")
    assert response.status_code == 200
    assert response.json() == empty_categories