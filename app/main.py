from library.library import Library
from models.employee import Employee
from validation.validation import validate_name, validate_age

def main():
    library = Library()

    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            if not validate_name(name):
                continue
            age = input("Enter age: ")
            if not age.isdigit() or not validate_age(int(age)):
                continue
            doj = input("Enter Date of Joining (YYYY-MM-DD): ")
            employee = Employee(name, int(age), doj)
            library.add_employee(employee)

        elif choice == '2':
            library.view_employees()

        elif choice == '3':
            name = input("Enter the name of the employee to update: ")
            new_name = input("Enter new name (leave blank to skip): ")
            new_age = input("Enter new age (leave blank to skip): ")
            new_age = int(new_age) if new_age.isdigit() else None
            library.update_employee(name, new_name, new_age)

        elif choice == '4':
            name = input("Enter the name of the employee to delete: ")
            library.delete_employee(name)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
