Feature: Create Todo
  As a user, I want to create an new todo 

  Background:
      Given the API is responsive
      And the database contains the default todo objects

  # Normal Flow

  Scenario Outline: Successfully create a new todo with only title
    When a new todo is created with title "<todo_name>"
    Then the status code 201 will be received
    Then a new todo exists in the database with title "<todo_name>"


  # Error Flow

  Scenario Outline: Create a new todo without a title
    When a new todo is created without a title
    Then the error <error> shall be raised with http status code <httpstatus>

    Examples:
        | error                      | httpstatus |
        | title : field is mandatory | 400        | 

  # Alternate Flow

  Scenario Outline: Successfully create a new todo with all feilds
    When a new todo is created with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" 
    Then the status code 201 will be received
    Then a new todo exists in the database with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" 


