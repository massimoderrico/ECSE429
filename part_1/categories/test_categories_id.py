import requests
from utils.cat_utils import *


def test_options_categories_id():
    response = requests.options(API_URL + "/categories/:id")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST, PUT, DELETE"


def test_head_categories_id():
    response = requests.head(API_URL + "/categories/1")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get category by id


def test_get_category_id_valid_id():
    id = 1
    response = requests.get(API_URL + "/categories/" + str(id))
    assert response.status_code == 200
    assert response.json() == {"categories": [default_categories["categories"][0]]}


def test_get_category_id_invalid_id():
    response = requests.get(API_URL + "/categories/" + str(invalid_cat_id))
    assert response.status_code == 404
    assert response.json() == cat_id_not_found_id


# Test put category with id


def test_put_category_id_invalid_id():
    response = requests.put(API_URL + "/categories/" + str(invalid_cat_id), json={})
    assert response.status_code == 404
    assert response.json() == cat_id_invalid_guid


def test_put_category_id_no_title():
    id = 1
    response = requests.put(API_URL + "/categories/" + str(id), json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_put_category_id_valid_payload():
    id = create_category({"title": cat_name}).get("id")
    response = requests.put(
        API_URL + "/categories/" + str(id),
        json={"title": cat_name, "description": cat_desc},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(id),
        "title": cat_name,
        "description": cat_desc,
    }
    delete_category(id)


def test_put_category_id_valid_with_id_in_payload():
    id = create_category({"title": cat_name}).get("id")
    random_id = 0
    response = requests.put(
        API_URL + "/categories/" + str(id),
        json={"id": str(random_id), "title": cat_name, "description": cat_desc},
    )
    print(response.status_code)
    assert response.status_code == 400
    assert response.json() == cat_id_put_id_in_payload_err
    delete_category(id)


def test_put_category_id_invalid_field_in_payload():
    id = create_category({"title": cat_name}).get("id")
    response = requests.put(
        API_URL + "/categories/" + str(id),
        json={"title": cat_name, "description": cat_desc, cat_bad_field: ""},
    )
    assert response.status_code == 400
    assert response.json() == cat_bad_field_err
    delete_category(id)


# Test post category with id


def test_post_category_id_invalid_id():
    response = requests.post(API_URL + "/categories/" + str(invalid_cat_id), json={})
    assert response.status_code == 404
    assert response.json() == cat_id_invalid_guid_or_id


def test_post_category_id_no_payload():
    id = 1
    response = requests.post(API_URL + "/categories/" + str(id), json={})
    assert response.status_code == 200
    assert response.json() == default_categories["categories"][0]


def test_post_category_id_valid_payload():
    id = create_category({"title": cat_name}).get("id")
    response = requests.post(
        API_URL + "/categories/" + str(id),
        json={"title": cat_name, "description": cat_desc},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(id),
        "title": cat_name,
        "description": cat_desc,
    }
    delete_category(id)


def test_post_category_id_valid_with_id_in_payload():
    id = create_category({"title": cat_name}).get("id")
    random_id = 0
    response = requests.post(
        API_URL + "/categories/" + str(id),
        json={"id": str(random_id), "title": cat_name, "description": cat_desc},
    )
    assert response.status_code == 400
    assert response.json() == cat_id_put_id_in_payload_err
    delete_category(id)


def test_post_category_id_invalid_field_in_payload():
    id = create_category({"title": cat_name}).get("id")
    response = requests.post(
        API_URL + "/categories/" + str(id),
        json={"title": cat_name, "description": cat_desc, cat_bad_field: ""},
    )
    assert response.status_code == 400
    assert response.json() == cat_bad_field_err
    delete_category(id)


# Test delete category by id


def test_delete_category_id_invalid_id():
    response = requests.delete(API_URL + "/categories/" + str(invalid_cat_id))
    assert response.status_code == 404
    assert response.json() == cat_id_delete_err


def test_delete_category_id_valid_id():
    id = create_category({"title": cat_name}).get("id")
    response = requests.delete(API_URL + "/categories/" + str(id))
    assert response.status_code == 200
    assert response.text == ""
