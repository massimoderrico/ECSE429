Feature: Modify Project
    As a user, I want to be able to modify a specific project

    Background:
        Given the API is responsive
        And the database contains the default project objects

    # Normal Flow
    Scenario Outline: Modify the description of a project
        When the user requests to modify the description of project "<id>" to "<description>"
        Then the status code "200" will be received
        Then the user will receive the modified project object with id "<id>", title "<title>", and description "<description>"

        Examples:
            | id | title       | description           |
            | 1  | Office Work | This is a description |

    # Alternate Flow
    Scenario Outline: Modify the title of a project
        When the user requests to modify the title of project "<id>" to "<title>"
        Then the status code "200" will be received
        Then the user will receive the modified project object with id "<id>", title "<title>", and description "<description>"

        Examples:
                | id | title           | description           |
                | 1  | New Office Work |       ""             |

    # Error Flow
    Scenario Outline: Modify a project that does not exist
        When the user requests to modify a project with invalid id "0"
        Then the status code "404" will be received
        Then the error "<error>" shall be raised with http status code "<httpstatus>"

        Examples:
            | error                                                    | httpstatus |
            | No such project entity instance with GUID or ID 0 found  | 404        |