import requests
from utils.utils import *


def test_options_projects():
    response = requests.options(API_URL + "/projects")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"
