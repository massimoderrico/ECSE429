Feature: Get Todos
     As a user, I want to be able to get todos given a search criteria

     Background:
         Given the API is responsive
         And the database contains the default todo objects

     # Normal Flow
     Scenario Outline: Get the todo matching an id
         When the user requests the todo with id <id>
         Then the status code 200 will be received
         Then the user will receive a todo with id <id>

         Examples:
             | id  |
             |  1  |

     # Alternate Flow
     Scenario Outline: Get all todos
         When the user requests to get all todos
         Then the status code 200 will be received
         Then the user will receive a list of all todos

     # Error Flow
     Scenario Outline: Get all todos matching an invalid todo id
         When the user requests to get all todos with invalid id 0
         Then the error <error> shall be raised with http status code <httpstatus>

         Examples:
             | error                                   | httpstatus |
             | Could not find an instance with todos/0 | 404        | 

   
    