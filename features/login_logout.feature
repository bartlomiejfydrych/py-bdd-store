Feature: login and logout

    Description:
    As user I want to login to page and logout

    Scenario: Correct login and logout
      Given open chrome browser on store site
      When click on sign in button
      And write login email address
      And write login password
      And click login sign in button
      Then user logged successfully
      And click sign out button