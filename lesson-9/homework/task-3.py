import csv
import json

class InvalidInputException(Exception):
    pass

def load_json():
    try:
        with open('tasks.json', 'r') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_task(tasks):
    with open('tasks.json', 'w') as json_file:
        json.dump(tasks, json_file, indent=4)

def view():
    try:
        content = load_json()
        if not content:
            print("No tasks found")
            return
        for task in content:
            print(f"ID: {task['id']}, Task Name: {task['task']}, Completed Status: {task['completed']}, Priority: {task['priority']}")
    except Exception as e:
        print(f"Error: {e}")

def modify(Task_id: int):
    tasks = load_json()
    for task in tasks:
        if task['id'] == Task_id:
            new_name = input("Enter new task name: ")
            task['task'] = new_name
            new_status = input("Is the task completed? (True/False): ").strip().lower()
            if new_status in ['true', 'false']:
                task['completed'] = new_status == 'true'
            else:
                raise InvalidInputException("Type only 'True' or 'False'")
            
            try:
                new_priority = int(input("Enter new priority (1-3): "))
                if new_priority not in [1, 2, 3]:
                    raise InvalidInputException("Type only (1-3)")
                task['priority'] = new_priority
            except ValueError:
                raise InvalidInputException("Priority must be a number between 1-3")
            
            save_task(tasks)
            print(f"Task with ID {task['id']} has been updated.")
            return
    print(f"Task with ID {Task_id} not found.")

def calculate_tasks():
    tasks = load_json()
    num_of_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    sum_priority = sum(task['priority'] for task in tasks)
    avg_priority = round(sum_priority / num_of_tasks, 2) if num_of_tasks > 0 else 0
    
    print(f"All tasks: {num_of_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Uncompleted Tasks: {num_of_tasks - completed_tasks}")
    print(f"Average priority: {avg_priority}")

def convert():
    tasks = load_json()
    with open('tasks.csv', 'w', newline='') as f:
        headers = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.writer(f)
        writer.writerow(headers)
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print('Tasks saved in tasks.csv')

if __name__ == '__main__':
    print("""
1. View Tasks
2. Modify Tasks
3. Calculate Tasks
4. Convert To CSV
5. Exit
""")
    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                view()
            elif choice == 2:
                try:
                    task_id = int(input("Enter Task ID: "))
                    modify(task_id)
                except ValueError:
                    print("Invalid input. Task ID must be a number.")
            elif choice == 3:
                calculate_tasks()
            elif choice == 4:
                convert()
            elif choice == 5:
                break
            else:
                print("Choose only from 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number from 1-5.")
