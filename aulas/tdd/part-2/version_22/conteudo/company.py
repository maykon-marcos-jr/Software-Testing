from employee import Employee
from project import Project
from occurence import Occurence, Occ_Priority, Occ_Type

class Company:
    def __init__(self, name:str) -> None:
        self.name = name
        self.employees = {}
        self.projects = {}

    def get_name(self) -> str:
        return self.name

    def add_employee(self, employee: Employee):
        if employee.get_name() in self.employees.keys():
            raise Exception("Employee already on Company")
        self.employees[employee.get_name()] = employee

    def get_employees(self) -> list[Employee]:
        return list(self.employees.values())

    def add_project(self, project: Project):
        if project.get_name() in self.projects.keys():
            raise Exception("Project already on Company")
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

    def create_occurence(
        self,
        key:str,
        name:str,
        project:str,
        leader:str,
        type:Occ_Type,
        priority:Occ_Priority,
        description:str,
    ) -> Occurence:

        if leader in self.employees.keys() and project in self.projects.keys():
            occ = Occurence(
                key=key,
                name=name,
                project=project,
                leader=leader,
                type=type,
                priority=priority,
                description=description,
            )
            self.employees[leader].add_occurence(occ)
            self.projects[project].add_occurence(occ)
            return occ
        else:
            raise Exception("Project or Employee not found")