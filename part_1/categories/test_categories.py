import requests
from utils.utils import *


# Test get categories
def test_get_categories_no_params():
    response = requests.get(API_URL + "/categories")
    assert response.status_code == 200
    assert response.json() == default_categories


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
    assert response.json() == default_categories


def test_get_categories_by_invalid_param_value():
    response = requests.get(API_URL + "/categories", params={"id": "0"})
    assert response.status_code == 200
    assert response.json() == empty_categories


def test_get_categories_by_inexistent_param():
    response = requests.get(API_URL + "/categories", params={"bad_key": "0"})
    assert response.status_code == 200
    assert response.json() == default_categories
