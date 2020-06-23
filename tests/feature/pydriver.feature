Feature: PyDriver
  Pylenium driver

  Scenario: Test Google search
    Given I visit https://google.com
    And I get [name='q'] element
    When I type puppies and hit Enter
    Then title should contain puppies

  Scenario: Test find single element with XPATH
    Given I visit https://google.com
    And I get //*[@name="q"] element with xpath
    When I type QA at the Point
    Then title should contain QA at the Point

  Scenario: Test hover and click to page transition
    Given I visit https://qap.dev
    When I hover a[href="/about"] element
    And I click a[href="/leadership"][class*=Header] element
    Then I should see Carlos Kidman on the page

  Scenario: Test Pylenium wait until
    Given I visit https://qap.dev
    And I wait for an element [href="/about"]
    Then element tag name should be a
    And I should be able to hover element

  Scenario: Test have URL
    Given I visit https://qap.dev
    Then I should be on https://www.qap.dev/

  @skip #(reason="hash tags causes errors")
  Scenario: Test html item b
    Given I visit https://www.google.pl/
    And I get gb_70 by id
    Then it should contain Sign in

  Scenario: Test viewport
    Given I visit https://google.com
    When I set window size to 1280 and 800
    Then window size should be 1280 and 800

  Scenario: H2 tag contains Share your blah blah blah
    Given I visit https://www.qap.dev/present-at-qap
    Then I should see Share your knowledge and experience with the community. in h2

  Scenario: Test should not find
    Given I visit https://google.com
    Then I should not find select

  Scenario: Test should not find by xpath
    Given I visit https://google.com
    Then I should not find //select by xpath

  Scenario: Test should not contain
    Given I visit https://google.com
    Then I should not see foobar