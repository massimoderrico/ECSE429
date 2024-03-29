import requests

API_URL = "http://localhost:4567"

# Default data
default_categories = {
    "categories": [
        {"id": "1", "title": "Office", "description": ""},
        {"id": "2", "title": "Home", "description": ""},
    ]
}
empty_categories = {"categories": []}
cat_name = "Cat_1"
cat_desc = "This is a nice cat"
invalid_cat_id = 0
cat_bad_field = "idd"

todo_name = "Todo_1"
todo_desc = "This is a nice todo"
empty_cat_todos = {"todos": []}
invalid_todo_id = 0



# Error messages
no_title_err = {"errorMessages": ["title : field is mandatory"]}
post_category_with_id = {
    "errorMessages": [
        "Invalid Creation: Failed Validation: Not allowed to create with id"
    ]
}
cat_bad_field_err = {"errorMessages": [f"Could not find field: {cat_bad_field}"]}
cat_id_not_found_id = {
    "errorMessages": [f"Could not find an instance with categories/{invalid_cat_id}"]
}
cat_id_invalid_guid = {
    "errorMessages": [f"Invalid GUID for {invalid_cat_id} entity category"]
}
cat_id_invalid_guid_or_id = {
    "errorMessages": [
        f"No such category entity instance with GUID or ID {invalid_cat_id} found"
    ]
}
cat_id_put_id_in_payload_err = {"errorMessages": ["Failed Validation: id should be ID"]}
cat_id_delete_err = {
    "errorMessages": [f"Could not find any instances with categories/{invalid_cat_id}"]
}
cat_invalid_id_todo_err = {
    "errorMessages": [
        f"Could not find parent thing for relationship categories/{invalid_cat_id}/todos"
    ]
}
cat_todo_with_id_err = {"errorMessages": ["Could not find thing matching value for id"]}
cat_todo_invalid_cat_id_err = {
    "errorMessages": [
        f"Could not find any instances with categories/{invalid_cat_id}/todos/{invalid_todo_id}"
    ]
}




# Helper functions
def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200



