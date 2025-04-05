import json
def view_tasks():
    try:
        with open("tasks.json",'r') as file:
            tasks = json.load(file)
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(f'[✓] {task["task"]}') if task["done"] else print(f'[ ] {task["task"]}')
            else:   
                print("No tasks found.")        
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")               

def add_tasks():
    tasks = []
    while True:
        task = input("Enter a task (or q for quit): ")
        if task.lower() == 'q':
            break
        done_input = input("Is the task done? (y/n): ")
        done = True if done_input.lower() == 'y' else False
        tasks.append({"task": task, "done": done})
        with open("tasks.json", 'w') as file:
            json.dump(tasks, file)
            print("Tasks saved successfully.")                   
def edit_tasks():
    pass
def delete_tasks():
    pass
def save_tasks():
    pass


def start():
    print("Welcome to the To-Do List App!")
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_tasks()
        elif choice == '3':
            edit_tasks()
        elif choice == '4':
            delete_tasks()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    add_tasks()