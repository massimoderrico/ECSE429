import requests
import xlsxwriter

API_URL = "http://localhost:4567"

header = 0
n_col = 0
tt_col = 1
c_time_col = 2
m_time_col= 3
d_time_col= 4
c_cpu_col = 5
m_cpu_col= 6
d_cpu_col= 7
c_mem_col = 8
m_mem_col= 9
d_mem_col= 10

# number of initial objects 
n = 100
workbook = xlsxwriter.Workbook('test_results.xlsx')
num_worksheets = 3

def init_worksheets():
    for cur_obj in range(0,num_worksheets,1):
        obj = ""
        assert cur_obj >=0 and cur_obj <= 2
        if cur_obj == 0:
            obj = "Todo"
        elif cur_obj == 1:
            obj = "Project"
        elif cur_obj == 2:
            obj = "Category"
        
        worksheet = workbook.add_worksheet(f"{obj} Results")
        worksheet.write(header, n_col, "Number of Objects")
        worksheet.write(header, tt_col, "Transaction Time")
        worksheet.write(header, c_time_col, f"Create {obj} Time")
        worksheet.write(header, m_time_col, f"Modify {obj} Time")
        worksheet.write(header, d_time_col, f"Delete {obj} Time")
        worksheet.write(header, c_cpu_col, f"Create {obj} CPU Usage")
        worksheet.write(header, m_cpu_col, f"Modify {obj} CPU Usage")
        worksheet.write(header, d_cpu_col, f"Delete {obj} CPU Usage")
        worksheet.write(header, c_mem_col, f"Create {obj} Memory Usage")
        worksheet.write(header, m_mem_col, f"Modify {obj} Memory Usage")
        worksheet.write(header, d_mem_col, f"Delete {obj} Memory Usage")
   

# Default data
default_todos = {
    "todos": [
        {
            "id": "1",
            "title": "scan paperwork",
            "doneStatus": "false",
            "description": "",
            "categories": [
                {
                    "id": "1"
                }
            ],
            "tasksof": [
                {
                    "id": "1"
                }
            ]
        },
        {
            "id": "2",
            "title": "file paperwork",
            "doneStatus": "false",
            "description": "",
            "tasksof": [
                {
                    "id": "1"
                }
            ]
        }
    ]
}

default_categories = {
    "categories": [
        { 
            "id": "1",
            "title": "Office", 
            "description": ""
        },
        {   
            "id": "2", 
            "title": "Home",
            "description": ""
        },
    ]
}

default_projects = {
    "projects": [
        {
            "id": "1", 
            "title": "Office Work", 
            "completed": 'false', 
            "active": 'false', "description": "", 
            "tasks": [
                {
                    "id": "1"
                },
                {
                    "id": "2"
                }
            ]
        }
    ]
}

# Todo dummy data
todo_payload = {
            "title": "Todo_1",
            "description": "This is a nice todo"
        }
todo_modified_payload = {
            "title": "Modified_Todo_1",
            "description": "This is not a nice modifed todo"
        }

# Project dummy data
project_payload = {
            "title": "Project_1",
            "description": "This is a nice project"
        }
project_modified_payload = {
            "title": "Modified_Project_1",
            "description": "This is not a nice modifed project"
        }

# Category dummy data
category_payload = {
            "title": "Category_1",
            "description": "This is a nice category"
        }
category_modified_payload = {
            "title": "Modified_Category_1",
            "description": "This is not a nice modifed category"
        }

# Todo helper functions
def get_todos():
    response = requests.get(API_URL + "/todos")
    assert response.status_code == 200
    return response.json()

def create_todo(payload):
    response = requests.post(API_URL + "/todos", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_todo(id, payload):
    response = requests.post(API_URL + f"/todos/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_todo(id):
    response = requests.delete(API_URL + f"/todos/{id}")
    assert response.status_code == 200

# Project helper functions

def create_project(payload):
    response = requests.post(API_URL + "/projects", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_project(id, payload):
    response = requests.post(API_URL + f"/projects/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_project(id):
    response = requests.delete(API_URL + f"/projects/{id}")
    assert response.status_code == 200

# Category helper functions
    
def create_category(payload):
    response = requests.post(API_URL + "/categories", json=payload)
    assert response.status_code == 201
    return response.json()

def modify_category(id, payload):
    response = requests.post(API_URL + f"/categories/{id}", json=payload)
    assert response.status_code == 200
    return response.json()

def delete_category(id):
    response = requests.delete(API_URL + f"/categories/{id}")
    assert response.status_code == 200


def create_object(object_type, payload):
    if object_type == 0:
        return create_todo(payload)
    elif object_type == 1:
        return create_project(payload)
    elif object_type == 2:
        return create_category(payload)
    else:
        return None

def modify_object(object_type, cur_id, payload):
    if object_type == 0:
        return modify_todo(cur_id, payload)
    elif object_type == 1:
        return modify_project(cur_id, payload)
    elif object_type == 2:
        return modify_category(cur_id, payload)
    else:
        return None

def delete_object(object_type, cur_id):
    if object_type == 0:
        return delete_todo(cur_id)
    elif object_type == 1:
        return delete_project(cur_id)
    elif object_type == 2:
        return delete_category(cur_id)
    else:
        return None
    
def payload_object(object_type):
    if object_type == 0:
        return todo_payload
    elif object_type == 1:
        return project_payload
    elif object_type == 2:
        return category_payload
    else:
        return None
    
def modified_payload_object(object_type):
    if object_type == 0:
        return todo_modified_payload
    elif object_type == 1:
        return project_modified_payload
    elif object_type == 2:
        return category_modified_payload
    else:
        return None
