class Project:
    def __init__(self, name:str) -> None:
        self.name =  name
        self.employees = []

    def get_name(self) -> str:
        return self.name

    def add_employee(self, employee_name:str):
        self.employees.append(employee_name)

    def get_employees(self) -> list[str]:
        return self.employees