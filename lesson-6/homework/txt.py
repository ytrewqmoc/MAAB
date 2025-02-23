import os

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!\n")

def view_employees():
    if not os.path.exists("employees.txt"):
        print("No records found.\n")
        return
    with open("employees.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.\n")
        else:
            for record in records:
                print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("Record Found: ", line.strip())
                return
    print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_lines = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                updated_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_lines.append(line)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_lines)
        print("Employee record updated successfully!\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_lines = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if not line.startswith(emp_id + ","):
                updated_lines.append(line)
            else:
                found = True
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_lines)
        print("Employee record deleted successfully!\n")
    else:
        print("Employee not found.\n")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
