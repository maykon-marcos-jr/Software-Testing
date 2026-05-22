"""
Uma empresa W possui vários funcionários e desenvolve vários projetos.
Um projeto tem uma coleção de ocorrências.

E uma ocorrência representa alguma coisa que precisa ser trabalhada.
Cada ocorrência tem um funcionário responsável, que precisa trabalhar no mesmo projeto da ocorrência
Cada funcionário pode trabalhar em vários projetos simultaneamente, e pode ser responsável por várias ocorrências.
Uma chave identifica unicamente uma ocorrência e um resumo mostra sobre o que trata a ocorrência.
Cada ocorrência pode estar em dois estados: aberta ou fechada.
Quando uma ocorrência é criada, ela é atribuída ao seu responsável e permanece no estado aberta enquanto o seu responsável não a termina.
Quando o responsável termina a ocorrência, ela é fechada.
O responsável pela ocorrência pode ser modificado somente enquanto a ocorrência está aberta.
▪ Existem diferentes tipos de ocorrências: tarefa, bug, refatoração.
▪ Cada ocorrência tem diferentes prioridades (alta, média, baixa) e estas prioridades podem ser modificadas somente enquanto a ocorrência está aberta.
▪ Cada funcionário pode ser responsável por, no máximo, 10 ocorrências abertas considerando todos os projetos nos quais ele participa

# História iniciais
Inclusão de ocorrência em um projeto
Modificação da prioridade de uma ocorrência
Modificação do responsável por uma ocorrência
Conclusão de uma ocorrência

Lista Inicial de Testes
Criação de uma ocorrência em um projeto
Criação de uma ocorrência em um projeto inexistente
Modificação do responsável por uma ocorrência
Conclusão de uma ocorrência
Conclusão de uma ocorrência já fechada
"""

# PYTHONPATH=conteudo:tests coverage run --branch -m unittest test_occurence_manager.TestOccurenceManager
# coverage report
# coverage html
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))


import unittest

from company import Company
from project import Project
from employee import Employee
from occurence import Occurence, Occ_Priority, Occ_Type

class TestOccurenceManager(unittest.TestCase):

    def create_employee(self, name:str="Maria") -> Employee:
        return Employee(name)

    def create_company(self, name:str="X") -> Company:
        return Company(name)

    def create_project(self, name:str="Expansão") -> Project:
        return Project(name)

    def create_occurence(self, company:Company=None, key="00",
            name="Limpeza", project="Producao", leader="Matheus",
            type=Occ_Type.TAREFA, priority=Occ_Priority.BAIXA,
            description="Varrer o Chão",
        ) -> Occurence:
        if company is None:
            company = self.create_company()
        return company.create_occurence(key, name, project, leader, type, priority, description)

    def test_create_company(self):
        name = "W"
        company = Company(name)
        self.assertEqual(name, company.get_name())

    def test_create_employee(self):
        name = "Jose"
        employee = Employee(name)
        self.assertEqual(name, employee.get_name())

    def test_add_employee_to_company(self):
        employee = self.create_employee()
        company = self.create_company()

        company.add_employee(employee)

        self.assertEqual(employee.get_name(), company.get_employees()[0].get_name())

    def test_add_multiple_employees_to_company(self):
        company = self.create_company()

        name1 = "João"
        employee1 = self.create_employee(name1)
        name2 = "Joana"
        employee2 = self.create_employee(name2)

        company.add_employee(employee1)
        company.add_employee(employee2)

        employees = company.get_employees()

        self.assertEqual(employee1.get_name(), employees[0].get_name())
        self.assertEqual(employee2.get_name(), employees[1].get_name())

    def test_create_project(self):
        name = "Vendas"
        project = Project(name)

        self.assertEqual(name, project.get_name())

    def test_add_project_to_company(self):
        company = self.create_company()

        project = self.create_project()

        company.add_project(project)

        projects = company.get_projects()

        self.assertEqual(project.get_name(), projects[0].get_name())

    def test_add_multiple_projects_to_company(self):
        company = self.create_company()

        project1 = self.create_project("Backend")
        project2 = self.create_project("Frontend")

        company.add_project(project1)
        company.add_project(project2)

        projects = company.get_projects()

        self.assertEqual(project1.get_name(), projects[0].get_name())
        self.assertEqual(project2.get_name(), projects[1].get_name())

    def test_add_employee_to_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())

        employees = company.get_employees_on_project(project.get_name())
        projects = company.get_employees()[0].get_projects()

        self.assertEqual(employee.get_name(), employees[0].get_name())
        self.assertEqual(project.get_name(), projects[0])

    def test_add_employee_to_invalid_project(self):
        company = self.create_company()
        employee = self.create_employee()

        company.add_employee(employee)
        with self.assertRaises(Exception):
            company.add_employee_to_project(employee.get_name(), "Vendas")

    def test_get_invalid_employee_on_project(self):
        company = self.create_company()
        project = self.create_project()
        company.add_project(project)

        with self.assertRaises(Exception):
            company.add_employee_to_project("Jose", project.get_name())

    def test_add_duplicated_employee(self):
        company = self.create_company()
        employee1 = self.create_employee()
        employee2 = self.create_employee()

        company.add_employee(employee1)

        with self.assertRaises(Exception):
            company.add_employee(employee2)

    def test_add_duplicated_project(self):
        company = self.create_company()
        project1 = self.create_project()
        project2 = self.create_project()

        company.add_project(project1)

        with self.assertRaises(Exception):
            company.add_project(project2)


    def test_create_task_high_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.TAREFA
        occ_priority = Occ_Priority.ALTA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_task_medium_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.TAREFA
        occ_priority = Occ_Priority.MEDIA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_task_low_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.TAREFA
        occ_priority = Occ_Priority.BAIXA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_bug_high_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.BUG
        occ_priority = Occ_Priority.ALTA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_bug_medium_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.BUG
        occ_priority = Occ_Priority.MEDIA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_bug_low_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.BUG
        occ_priority = Occ_Priority.BAIXA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_refator_high_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.REFATORACAO
        occ_priority = Occ_Priority.ALTA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_refator_medium_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.REFATORACAO
        occ_priority = Occ_Priority.MEDIA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_refator_low_occurence(self):
        company = self.create_company("Wallmart")
        project = self.create_project("Vendas-2")
        employee = self.create_employee("Lindson")

        company.add_employee(employee)
        company.add_project(project)

        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ_key = "032"
        occ_name = "excel"
        occ_description = "Transfer sales values to a excel sheet"
        occ_type = Occ_Type.REFATORACAO
        occ_priority = Occ_Priority.BAIXA

        occurence = company.create_occurence(
            key=occ_key,
            name=occ_name,
            project=project.get_name(),
            leader=employee.get_name(),
            type=occ_type,
            priority=occ_priority,
            description=occ_description,
        )

        self.assertEqual(occ_key, occurence.get_key())
        self.assertEqual(occ_name, occurence.get_name())
        self.assertEqual(occ_description, occurence.get_description())
        self.assertEqual(occ_type, occurence.get_type())
        self.assertEqual(occ_priority, occurence.get_priority())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_create_occurence_on_invalid_project_and_leader(self):
        with self.assertRaises(Exception):
            self.create_occurence(project="Non-Exist", leader="Not-Real")

    def test_create_occurence_on_invalid_project(self):
        company = self.create_company()
        employee = self.create_employee()
        company.add_employee(employee)
        with self.assertRaises(Exception):
            self.create_occurence(company=company, leader=employee.get_name(), project="Non-Exist")

    def test_create_occurence_on_invalid_leader(self):
        company = self.create_company()
        project = self.create_project()
        company.add_project(project)
        with self.assertRaises(Exception):
            self.create_occurence(company=company, leader="Non-Exist", project=project.get_name())

    def test_verify_occurence_is_on_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name())
        occurence = project.get_occurences()[0]

        self.assertEqual(occ.get_key(), occurence.get_key())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_verify_occurence_is_on_leader(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name())
        occurence = employee.get_occurences()[0]

        self.assertEqual(occ.get_key(), occurence.get_key())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    """
    Cada ocorrência tem um funcionário responsável, que precisa trabalhar no mesmo projeto da ocorrência
    Cada funcionário pode trabalhar em vários projetos simultaneamente, e pode ser responsável por várias ocorrências.
    Quando uma ocorrência é criada, ela é atribuída ao seu responsável e permanece no estado aberta enquanto o seu responsável não a termina.
    Quando o responsável termina a ocorrência, ela é fechada.
    O responsável pela ocorrência pode ser modificado somente enquanto a ocorrência está aberta.
    ▪ Cada ocorrência tem diferentes prioridades (alta, média, baixa) e estas prioridades podem ser modificadas somente enquanto a ocorrência está aberta.
    ▪ Cada funcionário pode ser responsável por, no máximo, 10 ocorrências abertas considerando todos os projetos nos quais ele participa
    """

    def test_add_multiple_occurences_for_same_leader_in_same_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_employee(employee)
        company.add_project(project)
        company.add_employee_to_project(employee.get_name(), project.get_name())


        occ1 = self.create_occurence(company=company, key="01", leader=employee.get_name(), project=project.get_name())
        occ2 = self.create_occurence(company=company, key="02", leader=employee.get_name(), project=project.get_name())
        occurence1, occurence2 = project.get_occurences()

        self.assertTrue(occurence1.is_open())
        self.assertTrue(occurence2.is_open())
        self.assertEqual(employee.get_name(), occurence1.get_leader())
        self.assertEqual(employee.get_name(), occurence2.get_leader())
        self.assertEqual(occ1.get_key(), occurence1.get_key())
        self.assertEqual(occ2.get_key(), occurence2.get_key())
        self.assertEqual(project.get_name(), occurence1.get_project())
        self.assertEqual(project.get_name(), occurence2.get_project())

    def test_add_occurence_for_a_leader_in_multiple_projects(self):
        company = self.create_company()
        project1 = self.create_project("p1")
        project2 = self.create_project("p2")
        employee = self.create_employee()
        company.add_employee(employee)
        company.add_project(project1)
        company.add_project(project2)
        company.add_employee_to_project(employee.get_name(), project1.get_name())
        company.add_employee_to_project(employee.get_name(), project2.get_name())


        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project1.get_name())
        occurence = employee.get_occurences()[0]

        self.assertEqual(occ.get_key(), occurence.get_key())
        self.assertEqual(employee.get_name(), occurence.get_leader())
        self.assertEqual(project1.get_name(), occurence.get_project())
        self.assertTrue(occurence.is_open())

    def test_add_multiple_occurences_for_same_leader_in_multiple_projects(self):
        company = self.create_company()
        project1 = self.create_project("p1")
        project2 = self.create_project("p2")
        employee = self.create_employee()
        company.add_employee(employee)
        company.add_project(project1)
        company.add_project(project2)
        company.add_employee_to_project(employee.get_name(), project1.get_name())
        company.add_employee_to_project(employee.get_name(), project2.get_name())


        self.create_occurence(company=company, key="01", leader=employee.get_name(), project=project1.get_name())
        self.create_occurence(company=company, key="02", leader=employee.get_name(), project=project2.get_name())
        occ1 = project1.get_occurences()[0]
        occ2 = project2.get_occurences()[0]
        occurence1, occurence2 = employee.get_occurences()

        self.assertTrue(occ1.is_open())
        self.assertTrue(occ2.is_open())
        self.assertEqual(employee.get_name(), occurence1.get_leader())
        self.assertEqual(employee.get_name(), occurence2.get_leader())
        self.assertEqual(occ1.get_key(), occurence1.get_key())
        self.assertEqual(occ2.get_key(), occurence2.get_key())
        self.assertEqual(project1.get_name(), occurence1.get_project())
        self.assertEqual(project2.get_name(), occurence2.get_project())

    def test_add_multiple_occurences_for_multiple_leaders_in_same_project(self):
        company = self.create_company()
        project = self.create_project()
        employee1 = self.create_employee("e1")
        employee2 = self.create_employee("e2")
        company.add_employee(employee1)
        company.add_employee(employee2)
        company.add_project(project)
        company.add_employee_to_project(employee1.get_name(), project.get_name())
        company.add_employee_to_project(employee2.get_name(), project.get_name())


        self.create_occurence(company=company, key="01", leader=employee1.get_name(), project=project.get_name())
        self.create_occurence(company=company, key="02", leader=employee2.get_name(), project=project.get_name())
        occ1, occ2 = project.get_occurences()
        occurence1 = employee1.get_occurences()[0]
        occurence2 = employee2.get_occurences()[0]

        self.assertTrue(occ1.is_open())
        self.assertTrue(occ2.is_open())
        self.assertEqual(employee1.get_name(), occurence1.get_leader())
        self.assertEqual(employee2.get_name(), occurence2.get_leader())
        self.assertEqual(occ1.get_key(), occurence1.get_key())
        self.assertEqual(occ2.get_key(), occurence2.get_key())
        self.assertEqual(project.get_name(), occurence1.get_project())
        self.assertEqual(project.get_name(), occurence2.get_project())

    def test_add_multiple_occurences_for_multiple_leaders_in_multiple_projects(self):
        company = self.create_company()
        project1 = self.create_project("p1")
        project2 = self.create_project("p2")
        employee1 = self.create_employee("e1")
        employee2 = self.create_employee("e2")
        company.add_employee(employee1)
        company.add_employee(employee2)
        company.add_project(project1)
        company.add_project(project2)
        company.add_employee_to_project(employee1.get_name(), project1.get_name())
        company.add_employee_to_project(employee2.get_name(), project2.get_name())


        self.create_occurence(company=company, key="01", leader=employee1.get_name(), project=project1.get_name())
        self.create_occurence(company=company, key="02", leader=employee2.get_name(), project=project2.get_name())
        occ1 = project1.get_occurences()[0]
        occ2 = project2.get_occurences()[0]
        occurence1 = employee1.get_occurences()[0]
        occurence2 = employee2.get_occurences()[0]

        self.assertTrue(occ1.is_open())
        self.assertTrue(occ2.is_open())
        self.assertEqual(employee1.get_name(), occurence1.get_leader())
        self.assertEqual(employee2.get_name(), occurence2.get_leader())
        self.assertEqual(occ1.get_key(), occurence1.get_key())
        self.assertEqual(occ2.get_key(), occurence2.get_key())
        self.assertEqual(project1.get_name(), occurence1.get_project())
        self.assertEqual(project2.get_name(), occurence2.get_project())

    def test_verify_leader_is_on_occurence_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)

        with self.assertRaises(Exception):
            self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name())

    def test_closed_occurence(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name())
        employee.finish_occurence(occ.get_key())

        self.assertFalse(occ.is_open())

    def test_change_occurence_priority(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name(), priority=Occ_Priority.BAIXA)
        employee.reset_priority(occ.get_key(), Occ_Priority.ALTA)

        self.assertEqual(occ.get_priority(), Occ_Priority.ALTA)

    def test_change_closed_occurence_priority(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        occ = self.create_occurence(company=company, leader=employee.get_name(), project=project.get_name(), priority=Occ_Priority.BAIXA)
        employee.finish_occurence(occ.get_key())
        with self.assertRaises(Exception):
            employee.reset_priority(occ.get_key(), Occ_Priority.ALTA)

    def test_change_occurence_leader(self):
        company = self.create_company()
        project = self.create_project()
        employee1 = self.create_employee("e1")
        employee2 = self.create_employee("e2")
        company.add_project(project)
        company.add_employee(employee1)
        company.add_employee(employee2)
        company.add_employee_to_project(employee1.get_name(), project.get_name())
        company.add_employee_to_project(employee2.get_name(), project.get_name())

        occ_or = self.create_occurence(company=company, leader=employee1.get_name(), project=project.get_name())
        company.change_leader(occ_key=occ_or.get_key(), new_leader=employee2.get_name())
        occ_new = employee2.get_occurences()[0]

        self.assertEqual(occ_or.get_key(), occ_new.get_key())
        self.assertEqual(occ_new.get_leader(), employee2.get_name())
        self.assertEqual(occ_or.get_leader(), occ_new.get_leader())
        self.assertTrue(occ_or.is_open())
        self.assertTrue(occ_new.is_open())

    def test_change_closed_occurence_leader(self):
        company = self.create_company()
        project = self.create_project()
        employee1 = self.create_employee("e1")
        employee2 = self.create_employee("e2")
        company.add_project(project)
        company.add_employee(employee1)
        company.add_employee(employee2)
        company.add_employee_to_project(employee1.get_name(), project.get_name())
        company.add_employee_to_project(employee2.get_name(), project.get_name())

        occ_or = self.create_occurence(company=company, leader=employee1.get_name(), project=project.get_name())
        employee1.finish_occurence(occ_or.get_key())
        with self.assertRaises(Exception):
            company.change_leader(occ_key=occ_or.get_key(), new_leader=employee2.get_name())

    def test_add_more_than_10_open_occurences_to_same_leader_same_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        with self.assertRaises(Exception):
            for i in range(11):
                self.create_occurence(key=f"{i}", company=company, leader=employee.get_name(), project=project.get_name())

    def test_add_11_occurences_1_closed_to_same_leader_same_project(self):
        company = self.create_company()
        project = self.create_project()
        employee = self.create_employee()
        company.add_project(project)
        company.add_employee(employee)
        company.add_employee_to_project(employee.get_name(), project.get_name())

        for i in range(11):
            self.create_occurence(key=f"{i}", company=company, leader=employee.get_name(), project=project.get_name())
            if i == 9:
                employee.finish_occurence(f"{i}")

    def test_add_more_than_10_open_occurences_to_same_leader_on_multiple_project(self):
        company = self.create_company()
        employee = self.create_employee()
        company.add_employee(employee)

        with self.assertRaises(Exception):
            for i in range(11):
                project = self.create_project(name=f"Proj-{i}")
                company.add_project(project)
                company.add_employee_to_project(employee.get_name(), project.get_name())
                self.create_occurence(key=f"{i}", company=company, leader=employee.get_name(), project=project.get_name())


if __name__ == '__main__':
    unittest.main()