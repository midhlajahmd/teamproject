class Employee:
    def __init__(self, name, age, doj, createdOn, isActive):
        self.name = name
        self.age = age
        self.doj = doj
        self.createdOn = createdOn
        self.isActive = isActive
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Date of Joining: {self.doj}")
        print(f"Created On: {self.createdOn}")
        print(f"Active or Inactive: {self.isActive}")