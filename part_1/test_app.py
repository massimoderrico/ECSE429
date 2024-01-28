import requests

API_URL = "http://localhost:4567"


def test_api_is_active():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"
