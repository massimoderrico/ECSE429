import pytest
import requests
from pytest_bdd import given, when, then, scenarios, parsers
from utils.todo_utils import *

# Define the scenario(s)
scenarios('../resources/delete_todos.feature')

# Normal Flow 

@when(parsers.parse("a new todo is created with title {title}"))
def create_todo_title(title, response):
    response["response"] = requests.post(
        API_URL + "/todos",
        json={"title": title},
    )

@then(parsers.parse("a new todo exists in the database with title {title}"))
def check_create_todo_title(title, response):
    todo = response["response"].json()   
    assert todo["title"] == title


#Alternate Flow

@when(parsers.parse("a new todo is created with title {title}, doneStatus {doneStatus} and description {description}"))
def create_todo_all(title, doneStatus, description, response):
    response["response"] = requests.post(
        API_URL + "/todos",
        json={"title": title,"doneStatus": doneStatus ,"description": description},
    )
  

@then(parsers.parse("a new todo exists in the database with title {title}, doneStatus {doneStatus} and description {description}"))
def check_create_todo_all(title, doneStatus, description, response):
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

# delete the created todo from the database
# @pytest.hookimpl
# def pytest_bdd_after_scenario(request,feature,scenario):



