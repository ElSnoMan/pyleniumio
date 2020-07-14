Feature: Driver Tests
  As a user of Pylenium
  I want to use py commands using Gherkin

  Scenario: Google Search Puppies
    Given I visit https://google.com
    When I search puppies
    Then the title should contain puppies

  Scenario: Google Search QA at the Point
    Given I visit https://google.com
    When I search QA at the Point
    Then the title should contain QA at the Point



  Scenario: Open Leadership Page using Header Menu
    Given I visit https://qap.dev
    When I open the Leadership Page
    Then I should see Carlos Kidman on the page