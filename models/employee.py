from datetime import datetime
class Employee:
    def __init__(self, name, age, doj, createdOn, isActive=True):
        self.name = name
        self.age = age
        self.doj = doj
        self.createdOn = datetime.now().strftime("%d-%m-%Y")
        self.isActive = isActive
    def display(self):
        print("--- Employee Details ---")
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Date of Joining: {self.doj}")
        print(f"Created On: {self.createdOn}")
        print(f"Active or Inactive: {self.isActive}")