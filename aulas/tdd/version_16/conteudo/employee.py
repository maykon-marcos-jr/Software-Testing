class Employee():
    def __init__(self, name:str) -> None:
        self.name = name
        self.projects = []

    def get_name(self) -> str:
        return self.name

    def join_project(self, project_name:str):
        self.projects.append(project_name)

    def get_projects(self):
        return self.projects