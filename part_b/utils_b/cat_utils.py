import requests

API_URL = "http://localhost:4567"


# Default data
default_categories = {
    "categories": [
        {"id": "1", "title": "Office", "description": ""},
        {"id": "2", "title": "Home", "description": ""},
    ]
}
empty_categories = {"categories": []}
cat_name = "Cat_1"


# Helper functions
def create_category(payload):
    response = requests.post(API_URL + "/categories", json=payload)
    assert response.status_code == 201
    return response.json()


def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200


def double_delete_cat_todo(cat_id, todo_id):
    response = requests.delete(API_URL + f"/categories/{cat_id}/todos/{todo_id}")
    assert response.status_code == 200
    response = requests.delete(API_URL + f"/todos/{todo_id}")
    assert response.status_code == 200


def double_delete_cat_project(cat_id, project_id):
    response = requests.delete(API_URL + f"/categories/{cat_id}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(API_URL + f"/projects/{project_id}")
    assert response.status_code == 200


def cleanup_cats():
    response = requests.get(API_URL + "/categories")
    assert response.status_code == 200
    categories = sorted(response.json()["categories"], key=lambda x: int(x["id"]))
    for cat in categories:
        # Default title and description
        default = [
            i
            for i in default_categories["categories"]
            if int(i["id"]) == int(cat["id"])
        ][0].copy()
        del default["id"]
        requests.post(
            API_URL + "/categories/" + cat["id"],
            json=default,
        )
        # Delete todos
        if "todos" in cat:
            for todo in cat["todos"]:
                double_delete_cat_todo(int(cat["id"]), int(todo["id"]))
        # Delete projects
        if "projects" in cat:
            for project in cat["projects"]:
                double_delete_cat_project(int(cat["id"]), int(project["id"]))