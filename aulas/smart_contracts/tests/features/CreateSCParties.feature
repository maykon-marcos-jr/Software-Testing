Feature: SC_AAA_BBB Creation

Background:
Given a contratante AAA Consultoria Empresarial Ltda.
  And a contratada BBB Tecnologia Ltda.
  And creation-date do contract é 2020/2/01

Scenario: Create o SC_AAA_BBB contract
Given a contratante AAA Consultoria Empresarial Ltda.
  And a contratada BBB Tecnologia Ltda.
  And a start-date do contract é 2020/2/16
  And a end-date do contract é 2020/3/18
 When contrato está criado
 Then o título do contrato deve ser SC_AAA_BBB
 Then a oblig1 deve ser criada
 Then a oblig2 deve ser criada
 Then a oblig3 deve ser criada
 Then a oblig4 deve ser criada
 Then a oblig5 deve ser criada
 Then a oblig6 deve ser criada
 Then a oblig7 deve ser criada


Scenario: Activate o SC_AAA_BBB contract
Given contrato está criado
  And a oblig1 é ativada
  And a oblig2 é ativada
  And a oblig3 é ativada
  And a oblig4 é ativada
  And a oblig5 é ativada
  And a oblig6 é ativada
  And a oblig7 é ativada
 When contrato é ativado
 Then a contratante deve assinar o contrato
 Then a contratada deve assinar o contrato