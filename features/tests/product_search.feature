Feature: Test Scenarios for Reelly

  Scenario: User is able to login to Reelly
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: ''
    When I input password: ''
    When I click button: Continue
    Then I verify page is displayed: Main Page

  Scenario: User is able to see social media icons
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: ''
    When I input password: ''
    When I click button: Continue
    When I click Menu Block button: Settings
    Then I see URL contains text: Settings
    When I click on button: Contact us
    Then I see URL contains text: contact-us