import requests
from utils.utils_todos import *


def test_options_todos_id():
    response = requests.options(API_URL + "/todos/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST, PUT, DELETE"


def test_head_todos_id():
    response = requests.head(API_URL + f"/todos/{valid_todo_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get todo by id


def test_get_todo_id_valid_id():
    response = requests.get(API_URL + "/todos/" + str(valid_todo_id))
    assert response.status_code == 200
    assert response.json() == {"todos": [default_todos["todos"][0]]}


def test_get_todo_id_invalid_id():
    response = requests.get(API_URL + "/todos/" + str(invalid_todo_id))
    assert response.status_code == 404
    assert response.json() == todo_id_not_found_id


# Test put todo with id


def test_put_todo_id_invalid_id():
    response = requests.put(API_URL + "/todos/" + str(invalid_todo_id), json={})
    assert response.status_code == 404
    assert response.json() == todo_id_invalid_guid


def test_put_todo_id_no_title():
    response = requests.put(API_URL + "/todos/" + str(valid_todo_id), json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_put_todo_id_valid_payload():
    id = create_todo({"title": todo_name}).get("id")
    response = requests.put(
        API_URL + "/todos/" + str(id),
        json={"title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(id),
        "title": todo_name,
        "doneStatus": todo_done_status,
        "description": todo_desc,
    }
    delete_todo(id)


def test_put_todo_id_valid_with_id_in_payload():
    id = create_todo({"title": todo_name}).get("id")
    random_id = 0
    response = requests.put(
        API_URL + "/todos/" + str(id),
        json={"id": str(random_id), "title": todo_name, "description": todo_desc},
    )
    print(response.status_code)
    assert response.status_code == 400
    assert response.json() == todo_id_put_id_in_payload_err
    delete_todo(id)


def test_put_todo_id_invalid_field_in_payload():
    id = create_todo({"title": todo_name}).get("id")
    response = requests.put(
        API_URL + "/todos/" + str(id),
        json={"title": todo_name, "description": todo_desc, todo_bad_field: ""},
    )
    assert response.status_code == 400
    assert response.json() == todo_bad_field_err
    delete_todo(id)


# # Test post todo with id


def test_post_todo_id_invalid_id():
    response = requests.post(API_URL + "/todos/" + str(invalid_todo_id), json={})
    assert response.status_code == 404
    assert response.json() == todo_id_invalid_guid_or_id


def test_post_todo_id_no_payload():
    response = requests.post(API_URL + "/todos/" + str(valid_todo_id), json={})
    assert response.status_code == 200
    assert response.json() == default_todos["todos"][0]


def test_post_todo_id_valid_payload():
    id = create_todo({"title": todo_name}).get("id")
    response = requests.post(
        API_URL + "/todos/" + str(id),
        json={"title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(id),
        "title": todo_name,
        "doneStatus": todo_done_status,
        "description": todo_desc,
    }
    delete_todo(id)


def test_post_todo_id_valid_with_id_in_payload():
    id = create_todo({"title": todo_name}).get("id")
    random_id = 0
    response = requests.post(
        API_URL + "/todos/" + str(id),
        json={"id": str(random_id), "title": todo_name, "description": todo_desc},
    )
    assert response.status_code == 400
    assert response.json() == todo_id_put_id_in_payload_err
    delete_todo(id)


def test_post_todo_id_invalid_field_in_payload():
    id = create_todo({"title": todo_name}).get("id")
    response = requests.post(
        API_URL + "/todos/" + str(id),
        json={"title": todo_name, "description": todo_desc, todo_bad_field: ""},
    )
    assert response.status_code == 400
    assert response.json() == todo_bad_field_err
    delete_todo(id)


# Test delete todo by id


def test_delete_todo_id_invalid_id():
    response = requests.delete(API_URL + "/todos/" + str(invalid_todo_id))
    assert response.status_code == 404
    assert response.json() == todo_id_delete_err


def test_delete_todo_id_valid_id():
    id = create_todo({"title": todo_name}).get("id")
    response = requests.delete(API_URL + "/todos/" + str(id))
    assert response.status_code == 200
    assert response.text == ""
