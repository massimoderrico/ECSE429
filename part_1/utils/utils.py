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
category_name = "Cat_1"
category_desc = "This is a nice cat"



# Error messages
post_category_no_title = {"errorMessages": ["title : field is mandatory"]}
post_category_with_id = {
    "errorMessages": [
        "Invalid Creation: Failed Validation: Not allowed to create with id"
    ]
}
post_category_bad_field = {"errorMessages": ["Could not find field: idd"]}




# Helper functions
def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200



