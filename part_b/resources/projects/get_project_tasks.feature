Feature: Get all tasks for a project
    As a user, I want to get all tasks for a project

    Background:
        Given the API is responsive
        And the database contains the default project objects
        And the database contains project with no tasks with title "Office Work II" and description "Work in the office" and completed "false" and active "false"
        
        # And the database contains the following project object with no tasks:
        #     | title | description | completed | active |
        #     | Office Work II | Work in the office |   false   | false|
    

    #Normal Flow
    Scenario Outline: Get all tasks for a project
        When the user requests all tasks for project "<id>"
        Then the status code "200" will be returned
        Then the user will receive a list of all tasks for project "<id>"

        Examples:
            | id | 
            | 1 | 

    #Alternate Flow
    Scenario Outline: Get no tasks for a project
        When the user requests all tasks for project with title "Office Work II"
        Then the status code "200" will be returned
        Then the user will receive an empty list of tasks


    #Error Flow
    Scenario Outline: Get all tasks for a project that does not exist
        When the user requests all tasks for project "100"
        Then the status code "200" will be returned
        Then the user will receive an empty list of tasks