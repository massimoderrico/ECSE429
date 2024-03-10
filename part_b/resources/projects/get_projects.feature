Feature: Get Projects
    As a user, I want to be able to get projects given a search criteria

    Background:
    Given the API is responsive
    And the database contains the default project objects
    
    # Normal Flow
    Scenario Outline: Get all projects
        When the user requests to get all projects
        Then the status code "200" will be received
        Then the user will receive a list of all projects

    #Alternate Flow
    Scenario Outline: Get all projects matching a title
        When the user requests to get all projects with title "Office Work"
        Then the status code "200" will be received
        Then the user will receive a list of all projects with title "Office Work"

    #Error FLow
    Scenario Outline: Get all projects matching an invalid project ID
        When the user requests to get all projects with an invalid id "0"
        Then the status code "200" will be received
        Then the user will receive an empty list of projects
    
