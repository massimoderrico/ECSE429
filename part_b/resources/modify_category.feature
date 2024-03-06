Feature: Modify Category
    As a user, I want to be able to modify a specific category

    Background:
        Given the API is responsive
        And the database contains the default category objects

    # Normal Flow
    Scenario Outline: Modify the description of a category
        When the user requests to modify the description of category <id> to description <description>
        Then the status code 200 will be received
        Then the user will receive the modified category object with id <id>, title <title>, and description <description>

        Examples:
            | id | title  | description        |
            | 1  | Office | This is a nice cat |

    # Alternate Flow
    Scenario Outline: Modify the title of a category
        When the user requests to modify the description of category <id> to title <title>
        Then the status code 200 will be received
        Then the user will receive the modified category object with id <id>, title <title>, and description <description>

        Examples:
            | id | title | description |
            | 2  | Cat_1 | ""          |

    # Error Flow
    Scenario Outline: Modify a category with an invalid category ID
        When the user requests to modify a category with invalid id 0
        Then the error <error> shall be raised with http status code <httpstatus>

        Examples:
            | error                                                    | httpstatus |
            | No such category entity instance with GUID or ID 0 found | 404        |