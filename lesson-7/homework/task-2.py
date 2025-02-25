import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass  # Create the file if it does not exist
    
    def add_employee(self, employee):
        if self.search_employee(employee.employee_id):
            print("Error: Employee ID must be unique.")
            return
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")
    
    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            employees = file.readlines()
        if not employees:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for emp in employees:
                print(emp.strip())
    
    def search_employee(self, employee_id):
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ','):
                    return line.strip()
        return None
    
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employees = []
        updated = False
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if data[0] == employee_id:
                    if name: data[1] = name
                    if position: data[2] = position
                    if salary: data[3] = salary
                    updated = True
                employees.append(', '.join(data))
        if updated:
            with open(self.FILE_NAME, 'w') as file:
                file.write('\n'.join(employees) + '\n')
            print("Employee updated successfully!")
        else:
            print("Employee ID not found.")
    
    def delete_employee(self, employee_id):
        employees = []
        deleted = False
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if not line.startswith(employee_id + ','):
                    employees.append(line.strip())
                else:
                    deleted = True
        if deleted:
            with open(self.FILE_NAME, 'w') as file:
                file.write('\n'.join(employees) + '\n')
            print("Employee deleted successfully!")
        else:
            print("Employee ID not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(emp_id, name, position, salary))
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                emp_id = input("Enter Employee ID to search: ")
                result = self.search_employee(emp_id)
                print(result if result else "Employee not found.")
            elif choice == '4':
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (leave blank to keep current): ") or None
                position = input("Enter new position (leave blank to keep current): ") or None
                salary = input("Enter new salary (leave blank to keep current): ") or None
                self.update_employee(emp_id, name, position, salary)
            elif choice == '5':
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
