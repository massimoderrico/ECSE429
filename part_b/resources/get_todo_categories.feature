Feature: Get all categories under a todo
     As a user, I want to get all categories under a todo

     Background:
         Given the API is responsive
         And the database contains the default todo objects

     # Normal Flow
     
     Scenario Outline: Get all categories under a todo
         Given the todo <todoID> has a category <categoryID>
         When the user requests to get all categories under todo <todoID>
         Then the status code 200 will be received
         Then the user will receive a list of all categories under todo <todoID>

         Examples:
             | todoID | categoryID |
             | 1      |     1      |

     # Alternate Flow
     Scenario Outline: Get no categories under a todo
         When the user requests to get all categories under todo <todoID>
         Then the status code 200 will be received
         Then the user will receive an empty list of categories

         Examples:
             | todoID |
             | 2      |

     # Error Flow
     Scenario Outline: Get all categories under invalid todo
         When the user requests to get all categories under todo <todoID>
         Then the status code 200 will be received
         Then the user will receive all categories under all todos

         Examples:
             |   todoID   |
             | 0          |