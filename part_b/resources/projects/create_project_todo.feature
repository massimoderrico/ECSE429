Feature: Create Project Todo
    As a user, I want to be able to create a todo linked to a project

    Background:
        Given the API is responsive
        And the database contains the default project objects

    # Normal FLow
    Scenario Outline: Create a project todo with only title
        When the user requests to create a todo with title "<title>" for project "<project_id>"
        Then the status code "201" will be received
        Then the user will receive the created todo object with title "<title>", done status "<done_status>", and description "<description>" for project "<project_id>"

    Examples:
            | project_id | title  | done_status | description |
            | 1          | Todo_1 | false      | "" |

    # Alternate Flow
    Scenario Outline: Create a project todo specifying all fields of todo
        When the user requests to create a todo with title "<title>", done status "<done_status>", and description "<description>" for project "<project_id>"
        Then the status code "201" will be received
        Then the user will receive the created todo object with title "<title>", done status "<done_status>", and description "<description>" for project "<project_id>"

    Examples:
            | project_id | title  | done_status | description |
            | 1          | Todo_2 | true       | This is a nice todo |

    
    # Error Flow
    Scenario Outline: Create a project todo without title
        When the user requests to create a todo for project "<project_id>" without title
        Then the error "<error>" shall be raised with http status code "<httpstatus>"

        Examples:
           | project_id | error                      | httpstatus |
            | 1 | title : field is mandatory | 400     |