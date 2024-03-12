import pytest
import requests
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.todo_utils import *

@pytest.fixture()
def reset_create_todo(response):
    yield 
    delete_todo(response["response"].json()["id"])

@scenario('../resources/create_todo.feature', 'Successfully create a new todo with only title')
def test_create_todo_normal():
    pass

@scenario('../resources/create_todo.feature', 'Successfully create a new todo with all fields')
def test_create_todo_alternative():
    pass

@scenario('../resources/create_todo.feature', 'Create a new todo without a title')
def test_create_todo_error():
    pass

# Normal Flow 

@when(parsers.parse("a new todo is created with title {title}"))
def create_todo_title(title, response):
    response["response"] = requests.post(
        API_URL + "/todos",
        json={"title": title}
    )

@then(parsers.parse("a new todo exists in the database with title {title}"))
def check_create_todo_title(title, response, reset_create_todo):
    todo = response["response"].json()   
    assert todo["title"] == title


#Alternate Flow

@when(parsers.parse("a new todo is created with title {title}, doneStatus {doneStatus} and description {description}"))
def create_todo_all( title, doneStatus, description, response):
    if doneStatus == "true":
        doneStatus = True
    else:
        doneStatus = False
    response["response"] = requests.post(
        API_URL + "/todos",
        json={"title": title, "doneStatus": doneStatus ,"description": description}
    )
  

@then(parsers.parse("a new todo exists in the database with title {title}, doneStatus {doneStatus} and description {description}"))
def check_create_todo_all(title, doneStatus, description, response, reset_create_todo):
    todo = response["response"].json()   
    assert todo["title"] == title
    assert todo["doneStatus"] == doneStatus
    assert todo["description"] == description

# Error Flow
    
@when("a new todo is created without a title")
def create_without_title(response):
        response["response"] = requests.post(
        API_URL + "/todos",
        json={},
    )



