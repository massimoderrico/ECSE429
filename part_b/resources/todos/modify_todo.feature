Feature: Modify Todo
     As a user, I want to be able to modify a specific todo

     Background:
         Given the API is responsive
         And the database contains the default todo objects

     # Normal Flow

     Scenario Outline: Modify the description of a todo
         When the user requests to modify the description of todo <id> to description <description>
         Then the status code 200 will be received
         Then the user will receive the modified todo object with id <id> and description <description>
         

         Examples:
             | id | description        |
             | 1  | This is a nice cat |

     # Alternate Flow
     Scenario Outline: Modify the title of a todo
         When the user requests to modify the title of todo <id> to title <title>
         Then the status code 200 will be received
         Then the user will receive the modified todo object with id <id> and title <title>
         

         Examples:
             | id | title | 
             | 1  | Cat_1 |

     # Error Flow

     Scenario Outline: Modify a todo with an invalid todo ID
         When the user requests to modify a todo with invalid id 0
         Then the error <error> shall be raised with http status code <httpstatus>

         Examples:
             | error                                                    | httpstatus |
             | No such todo entity instance with GUID or ID 0 found     | 404        |