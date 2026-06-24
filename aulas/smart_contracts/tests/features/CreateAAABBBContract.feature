Feature: SC_AAA_BBB Creation

Background:
Given the client named AAA
And the contractor named BBB
And the creation date is 10
And the contract title is SC_AAA_BBB


Scenario: Create the SC_AAA_BBB contract
Given the smart contract is created
When the smart contract is created
Then the smart contract must be created


Scenario: Activate the SC_AAA_BBB contract
Given I have created and deployed the smart contract
When I activate the smart contract
Then the smart contract is activated
And the start date must be 25
And the end date must be 55
And the client must be AAA
And the contractor must be BBB
And the client has paid the initial installment
