import requests
from utils.projects_utils import delete_project
from utils.cat_utils import *


def test_options_cat_id_projects_id():
    response = requests.options(API_URL + "/categories/:id/projects/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


# No matter the bad id, same response
def test_delete_cat_id_projects_id_invalid_id():
    response = requests.delete(
        API_URL + f"/categories/{invalid_cat_id}/projects/{invalid_project_id}"
    )
    assert response.status_code == 404
    assert response.json() == cat_project_invalid_cat_id_err


def test_delete_cat_id_projects_id_valid():
    cat_id = 1
    project_id = create_cat_project(
        cat_id, {"title": project_name, "description": project_desc}
    ).get("id")
    response = requests.delete(API_URL + f"/categories/{cat_id}/projects/{project_id}")
    assert response.status_code == 200
    assert response.text == ""
    delete_project(project_id)
