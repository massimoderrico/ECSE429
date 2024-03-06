import pytest
import requests
from utils.cat_utils import API_URL


@pytest.mark.run_first
def test_api_is_active():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"


@pytest.mark.run_last
def test_shutdown():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is already shutdown"
    try:
        response = requests.get(API_URL + "/shutdown")
    except requests.exceptions.ConnectionError:
        assert True
