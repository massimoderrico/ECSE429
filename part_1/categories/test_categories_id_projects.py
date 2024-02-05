import requests
from utils.projects_utils import delete_project
from utils.cat_utils import *


def test_options_cat_id_projects():
    response = requests.options(API_URL + "/categories/:id/projects")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_cat_id_projects():
    response = requests.head(API_URL + "/categories/:id/projects")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get projects by category id


def test_get_cat_id_projects_invalid_cat_id():
    cat_id = 1
    # Create under a good category
    project = create_cat_project(
        cat_id, {"title": project_name, "description": project_desc}
    )
    response = requests.get(API_URL + f"/categories/{invalid_cat_id}/projects")
    assert response.status_code == 200
    project_id = project.get("id")
    assert response.json() == {"projects": [project]}
    delete_cat_project(cat_id, project_id)
    delete_project(project_id)


def test_get_cat_id_projects_valid_cat_id_empty():
    cat_id = 1
    response = requests.get(API_URL + f"/categories/{cat_id}/projects")
    assert response.status_code == 200
    assert response.json() == empty_cat_projects


def test_get_cat_id_projects_for_one_cat_id():
    cat_id = 1
    other_cat_id = 2
    project = create_cat_project(
        cat_id, {"title": project_name, "description": project_desc}
    )
    response = requests.get(API_URL + f"/categories/{other_cat_id}/projects")
    assert response.status_code == 200
    project_id = project.get("id")
    assert response.json() == empty_cat_projects
    delete_cat_project(cat_id, project_id)
    delete_project(project_id)


# Test post projects by category id


def test_post_cat_id_projects_invalid_cat_id():
    response = requests.post(
        API_URL + "/categories/" + str(invalid_cat_id) + "/projects"
    )
    assert response.status_code == 404
    assert response.json() == cat_invalid_id_project_err


def test_post_cat_id_projects_no_title():
    cat_id = 1
    response = requests.post(API_URL + f"/categories/{cat_id}/projects", json={})
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert response.json() == {
        "id": project_id,
        "title": "",
        "completed": "false",
        "active": "false",
        "description": "",
    }
    delete_cat_project(cat_id, project_id)
    delete_project(project_id)


def test_post_cat_id_projects_valid_payload():
    cat_id = 1
    response = requests.post(
        API_URL + f"/categories/{cat_id}/projects",
        json={"title": project_name, "description": project_desc},
    )
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert response.json() == {
        "id": project_id,
        "title": project_name,
        "completed": "false",
        "active": "false",
        "description": project_desc,
    }
    delete_cat_project(cat_id, project_id)
    delete_project(project_id)


def test_post_cat_id_projects_id_in_payload():
    cat_id = 1
    response = requests.post(
        API_URL + f"/categories/{cat_id}/projects",
        json={"id": 1, "title": project_name, "description": project_desc},
    )
    assert response.status_code == 404
    assert response.json() == cat_project_with_id_err


def test_post_cat_id_projects_bad_field_in_payload():
    cat_id = 1
    response = requests.post(
        API_URL + f"/categories/{cat_id}/projects",
        json={"title": project_name, "description": project_desc, cat_bad_field: ""},
    )
    assert response.status_code == 400
    assert response.json() == invalid_field_err
