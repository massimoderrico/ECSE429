Feature: Delete todo
     As a user, I want to be able to delete instances of todos

     Background:
         Given the API is responsive
         And the database contains the default todo objects
         And the database contains the default category objects

     # Normal Flow
     
     Scenario Outline: Delete a todo
         Given the database contains a todo with <title>
         When the user requests to delete the todo with title <title>
         Then the status code 200 will be received with the text ""

         Examples:
             | title   |
             | Todo_1  |

    #  # Alternate Flow

      Scenario Outline: Delete a todo category
          Given the database contains a todo with <title>
          And the todo with title <title> has a category with id <catID>
          When the user requests to delete the category with id <catID> under todo with <title>
          Then the status code 200 will be received with the text ""

          Examples:
             | title  | catID |
             | Todo_1 |   2   |

      # Error Flow

      Scenario Outline: Delete a todo with invalid todo ID
         When the user requests to delete the todo with invalid ID 0 
         Then the error <error> shall be raised with http status code <httpstatus>

         Examples:
         | error                                     | httpstatus |
         | Could not find any instances with todos/0 | 404        |