class Employee:
    def __init__(self, employeename, age):
        self.employeeName = employeename
        self.age = age
    def display(self):
        print(f"Employee Name is: {self.employeename}")