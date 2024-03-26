import requests
import xlsxwriter
import time
from c_utils import *
 
workbook = xlsxwriter.Workbook('test_results.xlsx')
todo_worksheet = workbook.add_worksheet("Todo Results")

header = 0
tt_col = 0
n_col = 1
c_todo_time_col = 2
m_todo_time_col= 3
d_todo_time_col= 4
todo_worksheet.write(header, tt_col, 'Transaction Time')
todo_worksheet.write(header, n_col, 'Number of Objects')
todo_worksheet.write(header, c_todo_time_col, 'Create Todo Time')
todo_worksheet.write(header, m_todo_time_col, 'Modify Todo Time')
todo_worksheet.write(header, d_todo_time_col, 'Delete Todo Time')

def todo_sample():

    extra_object_ids = []
    current_object_id = None

    # number of initial objects 
    n = 10000 

    # starts from 0 initial objects in database to n
    for i in range(n+1):
        
        # create an extra dummy object in database
        if (i != 0):
            response = create_todo(todo_payload)
            extra_object_ids.append(response["id"])

        #start the timer
        start_time = time.time_ns()

        #create object and get creation time
        create_response = create_todo(todo_payload)
        current_object_id = create_response["id"]
        done_create = time.time_ns()

        #modify object and get modification time
        modify_response = modify_todo(current_object_id, todo_modified_payload)
        done_modify = time.time_ns()

        #delete object and get deletion time
        delete_response = delete_todo(current_object_id)
        done_delete = time.time_ns()

        create_time = done_create - start_time
        modify_time = done_modify - done_create
        delete_time = done_delete - done_modify
        total_time = done_delete - start_time

        todo_worksheet.write(i+1, tt_col, total_time/100000.0)
        todo_worksheet.write(i+1, n_col, i)
        todo_worksheet.write(i+1, c_todo_time_col, create_time/100000.0)
        todo_worksheet.write(i+1, m_todo_time_col, modify_time/100000.0)
        todo_worksheet.write(i+1, d_todo_time_col, delete_time/100000.0)


    # Clean Up Objects
    for extra_id in extra_object_ids:
        delete_todo(extra_id)
        
    # log results 
    workbook.close()

todo_sample()