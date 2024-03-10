Feature: Create Category Todo
    As a user, I want to be able to create a todo linked to a category

    Background:
        Given the API is responsive
        And the database contains the default category objects

    # Normal Flow
    Scenario Outline: Create a category todo with only title
        When the user requests to create a todo with title <title> under category <categoryID>
        Then the status code 201 will be received
        Then the user will receive the created todo object with title <title>, done status <doneStatus>, and description <description>

        Examples:
            | categoryID | title  | doneStatus | description |
            | 1          | Todo_1 | false      | ""          |

    # Alternate Flow
    Scenario Outline: Create a category todo specifying all fields of todos
        When the user requests to create a todo with title <title>,  done status <doneStatus>, and description <description> under category <categoryID>
        Then the status code 201 will be received
        Then the user will receive the created todo object with title <title>, done status <doneStatus>, and description <description>

        Examples:
            | categoryID | title  | doneStatus | description         |
            | 1          | Todo_1 | true       | This is a nice todo |

    # Error Flow
    Scenario Outline: Create a category todo without title
        When the user requests to create a todo with under category 1
        Then the error <error> shall be raised with http status code <httpstatus>

        Examples:
            | error                      | httpstatus |
            | title : field is mandatory | 400        |