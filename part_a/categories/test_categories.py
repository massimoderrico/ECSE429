import requests
from utils.cat_utils import *

def test_options_categories():
    response = requests.options(API_URL + "/categories")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_head_categories():
    response = requests.head(API_URL + "/categories")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == ""


# Test get categories
def test_get_categories_no_params():
    response = requests.get(API_URL + "/categories")
    assert response.status_code == 200
    assert {
        "categories": sorted(response.json()["categories"], key=lambda x: int(x["id"]))
    } == default_categories


def test_get_categories_by_valid_id():
    response = requests.get(API_URL + "/categories", params={"id": "1"})
    assert response.status_code == 200
    assert response.json() == {"categories": [default_categories["categories"][0]]}


def test_get_categories_by_valid_title():
    response = requests.get(API_URL + "/categories", params={"title": "Home"})
    assert response.status_code == 200
    assert response.json() == {"categories": [default_categories["categories"][1]]}


def test_get_categories_by_valid_description():
    response = requests.get(API_URL + "/categories", params={"description": ""})
    assert response.status_code == 200
    assert {
        "categories": sorted(response.json()["categories"], key=lambda x: int(x["id"]))
    } == default_categories


def test_get_categories_by_invalid_param_value():
    response = requests.get(API_URL + "/categories", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_categories


def test_get_categories_by_inexistent_param():
    response = requests.get(API_URL + "/categories", params={"bad_key": "0"})
    assert response.status_code == 200
    assert {
        "categories": sorted(response.json()["categories"], key=lambda x: int(x["id"]))
    } == default_categories


# Test post categories


def test_post_category_no_title():
    response = requests.post(API_URL + "/categories", json={})
    assert response.status_code == 400
    assert response.json() == no_title_err


def test_post_category_only_title():
    response = requests.post(API_URL + "/categories", json={"title": cat_name})
    assert response.status_code == 201
    delete_category(response.json()["id"])
    assert response.json()["title"] == cat_name


def test_post_category_with_title_and_id():
    response = requests.post(
        API_URL + "/categories", json={"id": "0", "title": cat_name}
    )
    assert response.status_code == 400
    assert response.json() == post_category_with_id


def test_post_category_with_title_desc():
    response = requests.post(
        API_URL + "/categories",
        json={"title": cat_name, "description": cat_desc},
    )
    assert response.status_code == 201
    delete_category(response.json()["id"])
    assert response.json()["title"] == cat_name
    assert response.json()["description"] == cat_desc


def test_post_category_with_bad_field():
    response = requests.post(
        API_URL + "/categories", json={"idd": "0", "title": cat_name}
    )
    assert response.status_code == 400
    assert response.json() == cat_bad_field_err
