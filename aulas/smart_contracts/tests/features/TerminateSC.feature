Feature: SC_AAA_BBB Termination

Scenario: Successful termination #1 of SC_AAA_BBB contract
Given the contractor has sent the invoice and report to the client
And the client indicated a technical responsible
And the client has no unpaid fines due to delays
When the contractor has fullfiled all requested services
And the client has paid the initial installment
And the client has paid the final installment
And the client has paid 20 hours at R$ 120 each until 90 days after the deliver date
Then the contract must be terminated
And the message must be Successful Termination

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given the contract is finished
When the contractor has not fullfiled all the requested services
Then the contract must be terminated
And the message must be Unsuccessful Termination

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given the contract is finished
When the contractor has not sent the invoice and report to the client
Then the contract must be terminated
And the message must be Unsuccessful Termination

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given the contract is finished
When the client has not paid the initial installment
Then the contract must be terminated
And the message must be Unsuccessful Termination

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
Given the contract is finished
When the client has not paid the final installment
Then the contract must be terminated
And the message must be Unsuccessful Termination