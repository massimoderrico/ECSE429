Feature: Get Categories
    As a user, I want to be able to get categories given a search criteria

    Background:
        Given the API is responsive
        And the database contains the default category objects

    # Normal Flow
    Scenario Outline: Get all categories
        When the user requests to get all categories
        Then the status code 200 will be received
        Then the user will receive a list of all categories

    # Alternate Flow
    Scenario Outline: Get all categories matching a title
        When the user requests to get all categories with title <title>
        Then the status code 200 will be received
        Then the user will receive a list of all categories with title <title>

        Examples:
            | title  |
            | Office |
            | Home   |

    # Error Flow
    Scenario Outline: Get all categories matching an invalid category ID
        When the user requests to get all categories with invalid id "0"
        Then the status code 200 will be received
        Then the user will receive an empty list of categories