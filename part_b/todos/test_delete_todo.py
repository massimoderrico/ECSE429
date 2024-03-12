import pytest
import requests
from pytest_bdd import given, when, then, scenario, parsers
from utils_b.todo_utils import *

@pytest.fixture()
def cleanup_tmp_todo(todos):
    yield
    delete_todo(todos["todos"][0].json()["id"])

@scenario('../resources/todos/delete_todo.feature', 'Delete a todo')
def test_delete_todo_normal():
    pass

@scenario('../resources/todos/delete_todo.feature', 'Delete a todo category')
def test_delete_todo_alternative():
    pass

@scenario('../resources/todos/delete_todo.feature', 'Delete a todo with invalid todo ID')
def test_delete_todo_error():
    pass

def get_todo_id_from_title(todo_title):
    response = requests.get(API_URL + "/todos")
    todos = response.json()["todos"]
    for todo in todos:
        if todo["title"] == todo_title:
            return todo["id"]
    return None
    
@given(parsers.parse("the database contains a todo with {title}"))
def database_create_todo_title(title, todos):
    response = requests.post(
        API_URL + "/todos",
        json={"title": title}
    )
    todos["todos"].append(response)
    assert response.status_code == 201
    assert response.json()["title"] == title
       

@when(parsers.parse("the user requests to delete the todo with title {title}"))
def delete_todo_with_title(title, response):
    response["response"] = requests.delete(API_URL + f"/todos/{get_todo_id_from_title(title)}")


@then(parsers.parse("the status code {status_code} will be received with the text {text}"))
def check_status_code(status_code, text, response):
    assert response["response"].status_code == int(status_code)
    assert response["response"].text == text.replace('"', "")


@given(parsers.parse("the todo with title {title} has a category with id {catID}"))
def create_category_link(title,catID):
    response = requests.post(API_URL + f"/todos/{get_todo_id_from_title(title)}/categories", json={"id": str(catID)})
    assert response.status_code == 201
    
@when(parsers.parse("the user requests to delete the category with id {catID} under todo with {title}"))
def delete_todo_cat(catID, title, response, cleanup_tmp_todo):
    response["response"] = requests.delete(API_URL + f"/todos/{get_todo_id_from_title(title)}/categories/{catID}")


@when(parsers.parse("the user requests to delete the todo with invalid ID {invalid_id}"))
def delete_todo_invalid_id(invalid_id, response):
    response["response"] = requests.delete(API_URL + f"/todos/{invalid_id}")