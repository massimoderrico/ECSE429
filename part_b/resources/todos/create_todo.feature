Feature: Create Todo
  As a user, I want to create an new todo 

  Background:
      Given the API is responsive
      And the database contains the default todo objects

  # Normal Flow

  Scenario Outline: Successfully create a new todo with only title
    When a new todo is created with title <title>
    Then the status code 201 will be received
    Then a new todo exists in the database with title <title>

    Examples:
      | title  |
      | Todo_1 | 

  # Alternate Flow

  Scenario Outline: Successfully create a new todo with all fields
    When a new todo is created with title <title>, doneStatus <doneStatus> and description <description> 
    Then the status code 201 will be received
    Then a new todo exists in the database with title <title>, doneStatus <doneStatus> and description <description> 

    Examples:
      | title  | doneStatus | description         |
      | Todo_1 |  false     | This is a nice todo |


  # Error Flow

  Scenario Outline: Create a new todo without a title
    When a new todo is created without a title
    Then the error <error> shall be raised with http status code <httpstatus>

    Examples:
      | error                      | httpstatus |
      | title : field is mandatory | 400        | 

