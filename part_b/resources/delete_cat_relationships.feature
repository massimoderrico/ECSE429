Feature: Delete instances of relationships with category
    As a user, I want to be able to delete instances of relationships associated with a category

    Background:
        Given the API is responsive
        And the database contains the default category objects
        And the database contains the category todo
            | categoryID | title  | doneStatus | description         |
            | 1          | Todo_1 | false      | This is a nice todo |
        And the database contains the category project
            | categoryID | title     | description            |
            | 2          | Project_1 | This is a nice project |

    # Normal Flow
    Scenario Outline: Delete a category todo
        When the user requests to delete the todo under category "1"
        Then the status code "200" will be received with the text ""

    # Alternate Flow
    Scenario Outline: Delete a category project
        When the user requests to delete the project under category "2"
        Then the status code "200" will be received with the text ""

    # Error Flow
    Scenario Outline: Delete a category todo with invalid category todo ID
        When the user requests to delete the todo with invalid ID "0" under the category "1"
        Then the error "<error>" shall be raised with http status code "<httpstatus>"

        Examples:
            | error                                                  | httpstatus |
            | Could not find any instances with categories/1/todos/0 | 404        |