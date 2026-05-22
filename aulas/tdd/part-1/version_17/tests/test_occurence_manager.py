"""
Uma empresa W possui vários funcionários e desenvolve vários projetos.
Cada funcionário pode trabalhar em vários projetos simultaneamente
e cada projeto pode ter vários funcionários

# História iniciais
Criação da empresa W
Inclusão de funcionário na empresa
Inclusão de projeto na empresa
Inclusão de funcionário da empresa em um projeto

Lista Inicial de Testes
Enumerar testes de criação da Empresa
Enumerar testes de criação de Funcionário e inclusão na empresa
Enumerar testes de criação de Projeto e inclusão na empresa
"""

# PYTHONPATH=conteudo:tests coverage run --branch -m unittest test_occurence_manager.TestOccurenceManager
# coverage report
# coverage html
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))


import unittest

from employee import Employee
from company import Company
from project import Project

class TestOccurenceManager(unittest.TestCase):

    def create_employee(self, name:str="Maria") -> Employee:
        return Employee(name)

    def create_company(self, name:str="X") -> Company:
        return Company(name)

    def create_project(self, name:str="Expansão") -> Project:
        return Project(name)

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


if __name__ == '__main__':
    unittest.main()