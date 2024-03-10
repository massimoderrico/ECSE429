from pytest_bdd import scenario, given, when, then, parsers
import requests
import pytest
from utils.utils import *
from utils.projects_utils import *
from .common_steps import *


def get_todo_id_from_title(todo_title):
    response = requests.get(API_URL + "/todos")
    todos = response.json()["todos"]
    for todo in todos:
        if todo["title"] == todo_title:
            return todo["id"]
    return None

def get_category_id_from_title(category_title):
    response = requests.get(API_URL + "/categories")
    categories = response.json()["categories"]
    for category in categories:
        if category["title"] == category_title:
            return category["id"]
    return None
    

def delete_project_category_relationship(category_title, project_id):
    response = requests.get(API_URL + "/projects/" + str(project_id) + "/categories")
    categories = response.json()["categories"]
    for category in categories:
        if category["title"] == category_title:
            # try deleting category from project
            response = requests.delete(API_URL + "/projects/" + str(project_id) + "/categories/" + str(category["id"]))
            if response.status_code != 200:
                print("Error deleting category from project: " + str(response.content))
            
            # try deleting category
            response = requests.delete(API_URL + "/categories/" + str(category["id"]))
            if response.status_code != 200:
                print("Error deleting category: " + str(response.content))

def delete_project_todo_relationship(todo_title, project_id):
    response = requests.get(API_URL + "/projects/" + str(project_id) + "/tasks")
    todos = response.json()["todos"]
    for todo in todos:
        if todo["title"] == todo_title:
            # try deleting todo from project
            response = requests.delete(API_URL + "/projects/" + str(project_id) + "/tasks/" + str(todo["id"]))
            if response.status_code != 200:
                print("Error deleting todo from project: " + str(response.content))
            
            # try deleting todo
            response = requests.delete(API_URL + "/todos/" + str(todo["id"]))
            if response.status_code != 200:
                print("Error deleting todo: " + str(response.content))



@pytest.fixture()
def context():
    return {}

@pytest.fixture()
def reset_database_with_project_relationship(scope='module'):
    yield
    delete_project_todo_relationship("Test Todo", 1)
    delete_project_category_relationship("Test Category", 1)


@scenario('delete_project_relationships.feature', 'Delete a project todo')
def test_delete_project_relationships_normal():
    pass

@scenario('delete_project_relationships.feature', 'Delete a project category')
def test_delete_project_relationships_category():
    pass

@scenario('delete_project_relationships.feature', 'Delete a project todo with invalid project todo ID')
def test_delete_project_relationships_error():
    pass

@given(parsers.parse('the database contains the project todo with title "{todo_title}" for default project'))
def given_project_todo(todo_title, reset_database_with_project_relationship):
    response = requests.post(API_URL + "/projects/1/tasks", json={"title": todo_title})
    assert response.status_code == 201

@given(parsers.parse('the database contains the project category with title "{category_title}" for default project'))
def given_project_category(category_title, reset_database_with_project_relationship):
    response = requests.post(API_URL + "/projects/1/categories", json={"title": category_title})
    assert response.status_code == 201

@when(parsers.parse('the user requests to delete the todo with title "Test Todo" for project "{project_id}"'))
def delete_project_todo_normal(project_id, context, reset_database_with_project_relationship):
    # get the todo id from the todo title
    todo_id = get_todo_id_from_title("Test Todo")

    response = requests.delete(API_URL + "/projects/" + str(project_id) + "/tasks/" + str(todo_id))
    
    context["response"] = response
    
    delete_project_todo_relationship("Test Todo", 1)


@when(parsers.parse('the user requests to delete the category with title "Test Category" for project "{project_id}"'))
def delete_project_category(project_id, context, reset_database_with_project_relationship):
    # get the category id from the category title
    category_id = get_category_id_from_title("Test Category")

    response = requests.delete(API_URL + "/projects/" + str(project_id) + "/categories/" + str(category_id))
    context["response"] = response
        
    delete_project_category_relationship("Test Category", 1)


@when(parsers.parse('the user requests to delete the todo with invalid ID "{id}" for the project "{project_id}"'))
def delete_project_relationships_error(id, project_id, context, reset_database_with_project_relationship):
    response = requests.delete(API_URL + "/projects/" + str(project_id) + "/tasks/" + str(id))
    context["response"] = response

@then(parsers.parse('the error "{error}" shall be raised with http status code "{httpstatus}"'))
def check_error_project_relationships(error, httpstatus, context, reset_database_with_project_relationship):
    response = context["response"]
    assert response.status_code == int(httpstatus)
    assert response.json()["errorMessages"][0] == error