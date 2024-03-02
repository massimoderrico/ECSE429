Feature: Create Todo
  I want to create an new todo for the todo list API 

  Background:
    Given the database contains the following todos:
    | title             | doneStatus | description        | categories | tasksof
    | scan paperwork    |    false   |                    | id: 1      | id: 1
    | file paperwork    |    false   |                    |            | id: 1

  # Normal Flow

  Scenario Outline: Successfully create a new todo
    When a new todo is created with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" 
    Then a new todo exists in the database with title "<todo_name>", doneStatus "<todo_done_status>" and description "<todo_desc>" 
    Then the number of todos in the database is "3"

    Examples:
      | firstname | lastname | email                | password       | authorities |
      | Mo        | Salah    | mo.salah@gmail.com   | MoIsAwesome01  | Moderator   |
      | Bob       | Marley   | bob.marley@gmail.com | BobIsAwesome01 | Moderator   |
