Feature: Test Scenarios for Reelly
  @smoke
  Scenario: User is able to login to Reelly
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: annabellechang95@gmail.com
    When I input password: Lingling1!
    When I click button: Continue
    Then I verify page is displayed: MainPage

  Scenario: User is able to see social media icons
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: annabellechang95@gmail.com
    When I input password: Lingling1!
    When I click button: Continue
    When I click Menu Block button: Settings
    Then I see URL contains text: settings
    When I click on button: Contact us
    Then I see URL contains text: contact-us
    Then I verify number of social media icons: 4