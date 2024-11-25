class admin:
    def __init__(self, adminName, age):
        self.adminName = adminName
        self.age = age
    def display(self):
        print(f"Admin Name is: {self.adminName}")