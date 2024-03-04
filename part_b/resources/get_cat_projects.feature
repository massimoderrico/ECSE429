Feature: Get all projects under a category
    As a user, I want to get all projects under a category

    Background:
        Given the API is responsive
        And the database contains the default category objects
        And the database contains the following category projects:
            | categoryID | title     | description            | completed | active |
            | 1          | Project_1 | This is a nice project | false     | true   |
            | 1          | Project_2 | This is a done project | true      | false  |

    # Normal Flow
    Scenario Outline: Get all projects under a category
        When the user requests to get all projects under category "<categoryID>"
        Then the status code "200" will be received
        Then the user will receive a list of all projects under category "<categoryID>"

    # Alternate Flow
    Scenario Outline: Get no project under a category
        When the user requests to get all projects under category "1"
        Then the status code "200" will be received
        Then the user will receive an empty list of projects

    # Error Flow
    Scenario Outline: Get all projects under invalid category
        When the user requests to get all projects under category "0"
        Then the status code "200" will be received
        Then the user will receive an empty list of projects