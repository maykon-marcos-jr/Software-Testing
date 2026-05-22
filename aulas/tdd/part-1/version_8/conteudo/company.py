from employee import Employee

class Company:
    def __init__(self, name:str) -> None:
        self.name = name
        self.employees = []

    def get_name(self) -> str:
        return self.name

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employees(self) -> list[Employee]:
        return self.employees