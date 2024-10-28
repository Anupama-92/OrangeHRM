  Feature: Login functionality
  Scenario: Successful login
    Given I am on the login page
    When I enter the username
    When I enter the password
    Then I should see the dashboard