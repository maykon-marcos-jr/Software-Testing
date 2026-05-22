from employee import Employee
from project import Project

class Company:
    def __init__(self, name:str) -> None:
        self.name = name
        self.employees = []
        self.projects = []

    def get_name(self) -> str:
        return self.name

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employees(self) -> list[Employee]:
        return self.employees

    def add_project(self, project: Project):
        self.projects.append(project)

    def get_projects(self) -> list[Project]:
        return self.projects