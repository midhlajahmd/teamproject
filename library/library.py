from models.employee import employee


class Library:
    def __init__(self):
        self.employees = [] 

    def add_employee(self, employee: employee):
        self.employees.append(employee)
        print("Employee added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
        for employee in self.employees:
            print(employee)

    def update_employee(self, name: str, new_name: str = None, new_age: int = None):
        for employee in self.employees:
            if employee.name == name:
                if new_name:
                    employee.name = new_name
                if new_age:
                    employee.age = new_age
                print(f"Employee '{name}' updated successfully.")
                return
        print(f"Employee '{name}' not found.")

    def delete_employee(self, name: str):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Employee '{name}' deleted successfully.")
                return
        print(f"Employee '{name}' not found.")
