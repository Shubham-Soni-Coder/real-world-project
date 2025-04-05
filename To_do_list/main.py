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
    try:
        # Load existing tasks from the file
        with open("tasks.json", 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []  # If the file doesn't exist, start with an empty list

    while True:
        task = input("Enter a task (or q to quit): ")
        if task.lower() == 'q':
            break

        done_input = input("Is the task done? (y/n): ")
        if done_input.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            continue
        done = True if done_input.lower() == 'y' else False
        tasks.append({"task": task, "done": done})

    # Save the updated tasks list back to the file
    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)
        print("Tasks saved successfully.")                   
def edit_tasks():
    try:
        # load tasks file
        with open("tasks.json",'r') as file:
            tasks = json.load(file)
            if tasks:
                if tasks:
                    print("Tasks:")
                    for i,task in enumerate(tasks):
                        print(f'{i+1}. [✓] {task["task"]}') if task["done"] else print(f'{i+1}. [ ] {task["task"]}')
            else:
                print("No tasks found.")
                return
        # # Get the task number to edit
        while True:
            print("what whould you like to do")
            print("1. Change task name")
            print("2. Change task status")
            print("3. Cancal")
            choice = input("Enter your choice : ")
            if int(choice) == 3:
                return "Cancelling..."
            elif choice.lower() not in ['1', '2']:
                print("Give choice in number")
            elif int(choice) == 1:
                choice = input("Enter your tasks number: ")
                if choice.isdigit() and 1 <= int(choice) <= len(tasks):
                    task_number = int(choice) - 1
                    new_task_name = input("Enter the new task name: ")
                    tasks[task_number]["task"] = new_task_name
                    with open("tasks.json",'w') as file:
                        json.dump(tasks,file,indent=4)
                        print(f"Task {task_number + 1} updated successfully.")            
                else: print("Invalid task number.")
            elif int(choice) == 2:
                choice = input("Enter your tasks number: ")
                if choice.isdigit() and 1 <= int(choice) <= len(tasks):
                    task_number = int(choice) - 1
                    new_task_name = input("Do you complete task y or n: ")
                    if new_task_name.lower() == 'y':
                        tasks[task_number]["done"] = True
                    elif new_task_name.lower() == 'n':
                        tasks[task_number]["done"] = False
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        continue
                    with open("tasks.json",'w') as file:
                        json.dump(tasks,file,indent=4)
                        print(f"Task {task_number + 1} updated successfully.")

    except FileNotFoundError:
        tasks = []


def marks_tasks():
    print("Mark All Tasks:")
    while True:
        print("1. Mark all as DONE")
        print("2. Mark all as NOT DONE")
        print("3. Cancel")
        choice = input("Choose an option:")
        if choice == '1':
            # Mark all tasks as done
            with open("tasks.json",'r') as file:
                tasks = json.load(file)
                for task in tasks:
                    task["done"] = True
            with open("tasks.json",'w') as file:
                json.dump(tasks,file,indent=4)
                print("All tasks marked as done.\n")
        elif choice == '2':
            # Mark all tasks as not done
            with open("tasks.json",'r') as file:
                tasks = json.load(file)
                for task in tasks:
                    task["done"] = False
            with open("tasks.json",'w') as file:
                json.dump(tasks,file,indent=4)
                print("All tasks marked as not done.\n")
        elif choice == '3':
            return "Cancelling..."
        else:
            print("Invalid choice.\n")
def delete_tasks():
    pass
def save_tasks():
    pass


def start():
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. View Tasks")
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
    marks_tasks()