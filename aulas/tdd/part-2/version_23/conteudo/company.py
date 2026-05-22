from employee import Employee
from project import Project
from occurence import Occurence, Occ_Priority, Occ_Type

class Company:
    def __init__(self, name:str) -> None:
        self.__name = name
        self.__employees = {}
        self.__projects = {}
        self.__occurences = {}

    def get_name(self) -> str:
        return self.__name

    def add_employee(self, employee: Employee):
        if employee.get_name() in self.__employees.keys():
            raise Exception("Employee already on Company")
        self.__employees[employee.get_name()] = employee

    def get_employees(self) -> list[Employee]:
        return list(self.__employees.values())

    def add_project(self, project: Project):
        if project.get_name() in self.__projects.keys():
            raise Exception("Project already on Company")
        self.__projects[project.get_name()] = project

    def get_projects(self) -> list[Project]:
        return list(self.__projects.values())

    def add_employee_to_project(self, employee_name:str, project_name:str):
        if employee_name in self.__employees.keys() and project_name in self.__projects.keys():
            pj = self.__projects[project_name]
            pj.add_employee(employee_name)
            em = self.__employees[employee_name]
            em.join_project(project_name)
        else:
            raise Exception("Project or Employee not found")

    def get_employees_on_project(self, project_name:str) -> list[Employee]:
        ep = [self.__employees[name] for name in self.__projects[project_name].get_employees()]
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

        if leader in self.__employees.keys() and project in self.__projects.keys() and leader in self.__projects[project].get_employees():
            leader_ins = self.__employees[leader]
            count = 0
            for o in leader_ins.get_occurences():
                if o.is_open():
                    count += 1
            if count >= 10:
                raise Exception("To many occurences at once")

            occ = Occurence(
                key=key,
                name=name,
                project=project,
                leader=leader,
                type=type,
                priority=priority,
                description=description,
            )
            leader_ins.add_occurence(occ)
            self.__projects[project].add_occurence(occ)
            self.__occurences[key] = occ
            return occ
        else:
            raise Exception("Project or Employee not found")

    def change_leader(self, occ_key:str, new_leader:str):
        if new_leader in self.__employees.keys() and occ_key in self.__occurences.keys():
            occ = self.__occurences[occ_key]
            cur_leader = self.__employees[occ.get_leader()]
            cur_leader.leave_occurence(occ_key, new_leader)
            self.__employees[new_leader].add_occurence(occ)