Feature: Delete todo
     As a user, I want to be able to delete instances of todos

     Background:
         Given the API is responsive
         And the database contains the default todo objects
         And the database contains the category todo with title Todo_1, done status false, and description This is a nice todo under category 1
         # | id         | title  | doneStatus | description         |
         # | 1          | Todo_1 | false      | This is a nice todo |

     # Normal Flow
     Scenario Outline: Delete a todo
         When the user requests to delete the todo under id <id>
         Then the status code 200 will be received with the text ""

         Examples:
             | id |
             | 1  |

     # Alternate Flow
     Scenario Outline: Delete a todo taskOf
         When the user requests to delete the taskOf with id <taskOfID> under todo id <todoID>
         Then the status code 200 will be received with the text ""

         Examples:
             | categoryID |
             | 2          |

     # Error Flow

     Scenario Outline: Delete a todo with invalid todo ID
         When the user requests to delete the todo with invalid ID 0 
         Then the error <error> shall be raised with http status code <httpstatus>

         Examples:
             | error                                     | httpstatus |
             | Could not find any instances with todos/0 | 404        |