import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title: task.title = title
                if description: task.description = description
                if due_date: task.due_date = due_date
                if status: task.status = status
                self.storage.save_tasks(self.tasks)
                print("Task updated successfully!")
                return
        print("Task ID not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage.save_tasks(self.tasks)
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status == status]
        if not filtered:
            print("No tasks with the given status.")
        else:
            for task in filtered:
                print(task)

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
                status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                self.add_task(Task(task_id, title, description, due_date, status))
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new title (leave blank to keep current): ") or None
                description = input("Enter new description (leave blank to keep current): ") or None
                due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ") or None
                status = input("Enter new status (leave blank to keep current): ") or None
                self.update_task(task_id, title, description, due_date, status)
            elif choice == '4':
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)
            elif choice == '5':
                status = input("Enter status to filter by (Pending/In Progress/Completed): ")
                self.filter_tasks(status)
            elif choice == '6':
                self.storage.save_tasks(self.tasks)
                print("Tasks saved successfully!")
            elif choice == '7':
                self.tasks = self.storage.load_tasks()
                print("Tasks loaded successfully!")
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

class JSONStorage:
    FILE_NAME = "tasks.json"
    
    def load_tasks(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                data = json.load(file)
                return [Task(**task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

class CSVStorage:
    FILE_NAME = "tasks.csv"
    
    def load_tasks(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                reader = csv.DictReader(file)
                return [Task(**row) for row in reader]
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, 'w', newline='') as file:
            fieldnames = ["task_id", "title", "description", "due_date", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

if __name__ == "__main__":
    storage_type = input("Choose storage format (json/csv): ").strip().lower()
    storage = JSONStorage() if storage_type == "json" else CSVStorage()
    manager = TaskManager(storage)
    manager.menu()
