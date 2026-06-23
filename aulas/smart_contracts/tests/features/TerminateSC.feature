Feature: SC_AAA_BBB Termination

Scenario: Successful termination #1 of SC_AAA_BBB contract
    Given não violação da oblig2
      And não violação da oblig3
      And não violação da oblig6
    When oblig1 for concluida
      And oblig4 for concluida
      And oblig5 for concluida
    Then a contratante deve cumprir a oblig7
      And todas as oblig sobreviventes devem estar concluidas
      And o contrato deve ser terminado

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
    Given atingiu-se a data de término do contrato
    When oblig1 é violada
    Then todas as oblig sobreviventes devem ser desativadas
      And o contrato deve ser terminado

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
    Given atingiu-se a data de término do contrato
      And não violação da oblig1
    When oblig2 é violada
    Then todas as oblig sobreviventes devem ser desativadas
      And o contrato deve ser terminado

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
    Given atingiu-se a data de criação do contrato
    When oblig4 é violada
    Then todas as oblig sobreviventes devem ser desativadas
      And o contrato deve ser terminado

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
    Given atingiu-se a data de término do contrato
      And não violação da oblig1
      And não violação da oblig2
    When oblig5 é violada
    Then todas as oblig sobreviventes devem ser desativadas
      And o contrato deve ser terminado