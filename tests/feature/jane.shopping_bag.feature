Feature: Shopping Bag
  As a shopper I want to add things to my cart
  so I can keep track of what I want to order.

  Background:
    Given I am on the Jane Home Page

  Scenario: Adding an item updates the Shopping Bag Icon
    When I add 1 item to my cart
    Then I should see the Shopping Bag Icon go up by 1

  @jane
  Scenario: Adding an item updates the Cart Page
    When I add 1 item to my cart
    Then I should see the item in the cart

  Scenario: Deleting an item from the Cart Page
    When I delete 1 item from the cart
    Then the totals should adjust automatically