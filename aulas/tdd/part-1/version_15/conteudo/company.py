from employee import Employee
from project import Project

class Company:
    def __init__(self, name:str) -> None:
        self.name = name
        self.employees = {}
        self.projects = {}

    def get_name(self) -> str:
        return self.name

    def add_employee(self, employee: Employee):
        self.employees[employee.get_name()] = employee

    def get_employees(self) -> list[Employee]:
        return list(self.employees.values())

    def add_project(self, project: Project):
        self.projects[project.get_name()] = project

    def get_projects(self) -> list[Project]:
        return list(self.projects.values())

    def add_employee_to_project(self, employee_name:str, project_name:str):
        if employee_name in self.employees.keys() and project_name in self.projects.keys():
            pj = self.projects[project_name]
            pj.add_employee(employee_name)
            em = self.employees[employee_name]
            em.join_project(project_name)
        else:
            raise Exception("Project or Employee not found")

    def get_employees_on_project(self, project_name:str) -> list[Employee]:
        ep = [self.employees[name] for name in self.projects[project_name].get_employees()]
        return ep