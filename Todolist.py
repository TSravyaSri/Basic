tasks = {}  # Dictionary to store tasks
def add_task(task_id, task_description):
    tasks[task_id] = task_description
    print(f"Task {task_id} added: {task_description}")
def complete_task(task_id):
    if task_id in tasks:
        print(f"Task {task_id} completed: {tasks[task_id]}")
        del tasks[task_id]
    else:
        print(f"Task {task_id} not found.")
def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} removed.")
    else:
        print(f"Task {task_id} not found.")
def print_tasks():
    if tasks:
        print("Tasks:")
        for task_id, task_description in tasks.items():
            print(f"{task_id}: {task_description}")
    else:
        print("No tasks found.")
# Main program loop
while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. Print Tasks")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        task_id = input("Enter task ID: ")
        task_description = input("Enter task description: ")
        add_task(task_id, task_description)
    elif choice == '2':
        task_id = input("Enter task ID to complete: ")
        complete_task(task_id)
    elif choice == '3':
        task_id = input("Enter task ID to remove: ")
        remove_task(task_id)
    elif choice == '4':
        print_tasks()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
