Feature: Delete instances of relationships with a project
    As a user, I want to be able to delete instances of relationships associated with a project

    Background:
        Given the API is responsive
        And the database contains the default project objects
        And the database contains the project todo with title "Test Todo" for default project
        And the database contains the project category with title "Test Category" for default project

   # Normal Flow
    Scenario Outline: Delete a project todo
        When the user requests to delete the todo with title "Test Todo" for project "1"
        Then the status code "200" will be received

    # Alternate Flow
    Scenario Outline: Delete a project category
        When the user requests to delete the category with title "Test Category" for project "1"
        Then the status code "200" will be received

    # Error Flow
    Scenario Outline: Delete a project todo with invalid project todo ID
        When the user requests to delete the todo with invalid ID "0" for the project "1"
        Then the error "<error>" shall be raised with http status code "<httpstatus>"

        Examples:
            | error                                                  | httpstatus |
            | Could not find any instances with projects/1/tasks/0 | 404        |