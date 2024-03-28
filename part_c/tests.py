import requests
import time
from c_utils import *
import psutil
import pytest

@pytest.mark.run_first
def test_api_is_active():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API is not active"

@pytest.mark.run_first
def test_worksheet_created():
    init_worksheets()
    assert len(workbook.worksheets()) == num_worksheets

# def test_object_transaction(cur_obj, worksheet):

#     object_ids = []
#     current_object_id = None

#     # starts from 0 initial objects in database to n
#     for i in range(0, n+1, 1):
        
#         # create an extra dummy object in database
#         if (i != 0):
#             response = create_object(cur_obj, payload_object(cur_obj))
#             object_ids.append(response["id"])

#         #start the timer
#         start_time = time.time_ns()

#         #create object 
#         create_response = create_object(cur_obj, payload_object(cur_obj))
#         current_object_id = create_response["id"]
#         #modify object 
#         modify_object(cur_obj, current_object_id, todo_modified_payload)
#         #delete object 
#         delete_object(cur_obj, current_object_id)
        
#         # stop timer and get delta time
#         done_time = time.time_ns()
#         total_time = done_time - start_time
    
#         #log to worksheet
#         worksheet.write(i+1, tt_col, total_time/100000.0)

#     # Clean Up Objects
#     for extra_id in object_ids:
#         delete_object(cur_obj, extra_id)

@pytest.mark.parametrize("cur_obj", range(num_worksheets))
def test_object_create(cur_obj):
    # list to save ids
    object_ids = []
    worksheet = workbook.worksheets()[cur_obj]
    # starts from 0 initial objects in database to n
    for i in range(n+1):
        start_time = time.time_ns()
        # start_cpu = psutil.cpu_percent()
        # start_mem = psutil.virtual_memory().used
        response = create_object(cur_obj, payload_object(cur_obj))
        # done_mem = psutil.virtual_memory().used
        # done_cpu = psutil.cpu_percent()
        done_create = time.time_ns()

        #save created id
        object_ids.append(response["id"])

        #get time delta
        create_time = done_create - start_time
        #get cpu usage
        # cpu_used = start_cpu - done_cpu
        #get memory usage
        # mem_used = start_mem - done_mem

        #log all data in excel file
        
        worksheet.write(i+1, n_col, i)
        worksheet.write(i+1, c_time_col, create_time/100000.0)
        # worksheet.write(i+1, c_cpu_col, cpu_used)
        # worksheet.write(i+1, c_mem_col, mem_used)
        
    # Clean Up Objects
    for extra_id in object_ids:
        delete_object(cur_obj, extra_id)
    
    assert True

# def object_delete(cur_obj, worksheet):
     # list to save ids
    object_ids = []

    # starts from 0 initial objects in database to n
    for i in range(0, n+1, 1):
        response = create_object(cur_obj, payload_object(cur_obj))
        #save ids
        object_ids.append(response["id"])
        
    for i in range( n, -1, -1):
        #start_time
        start_time = time.time_ns()
        delete_object(cur_obj, object_ids[i])
        #stop time
        done_delete = time.time_ns()

        #get time delta and write to excel file
        delete_time = done_delete - start_time
        worksheet.write(i+1, n_col, i)
        worksheet.write(i+1, d_time_col, delete_time/100000.0)

# def object_modify(cur_obj, worksheet):

#     # list to save ids
#     object_ids = []
#     current_object_id = None

#     # starts from 0 initial objects in database to n
#     for i in range(0, n+1, 1):
        
#         # create an dummy object in database
#         response = create_object( cur_obj, payload_object(cur_obj))
#         current_object_id = response["id"]
#         object_ids.append(current_object_id)

#         #start time
#         start_time = time.time_ns()
#         #stop time
#         modify_object(cur_obj, current_object_id, modified_payload_object(cur_obj))
#         done_modify = time.time_ns()

#         #get time delta and write to excel file
#         modify_time = start_time - done_modify 
#         worksheet.write(i+1, n_col, i)
#         worksheet.write(i+1, m_time_col, modify_time/100000.0)

#     # Clean Up Objects
#     for extra_id in object_ids:
#         delete_object(cur_obj, extra_id)


@pytest.mark.run_last
def test_close_workbook():
    workbook.close()

