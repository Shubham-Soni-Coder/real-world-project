import json

def update_all_tasks(done_status):
    with open("tasks.json",'r') as file:
        tasks = json.load(file)
        for task in tasks:
            task["done"] = done_status
    with open("tasks.json",'w') as file:
        json.dump(tasks,file,indent=4)    

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks,numbered=True):
    for i,task in enumerate(tasks):
        prefix = f'{i+1}.' if numbered else ''
        status = '[✓]' if task['done'] else '[ ]'
        print(f"{prefix}{status} {task['task']}")

def view_tasks():
    try:
        with open("tasks.json",'r') as file:
            tasks = json.load(file)
            if tasks:
                print("Tasks:")
                display_tasks(tasks,numbered=False)
            else:   
                print("No tasks found.")        
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")               

def add_tasks():
    tasks = load_tasks()
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
    save_tasks(tasks)
    print("Tasks saved successfully.")                   
def edit_tasks():
        tasks = load_tasks()
        if tasks:
            print("Tasks:")
            display_tasks(tasks)
        else:
            print("No tasks found.")
            return
        # # Get the task number to edit
        while True:
            print("what whould you like to do")
            print("1. Change task name")
            print("2. Change task status")
            print("3. Cancel")
            choice = input("Enter your choice : ")
            if choice == '3':
                print("Cancelling...")
                return
            elif choice.lower() not in ['1', '2']:
                print("Give choice in number")
            elif choice == '1':
                choice = input("Enter your tasks number: ")
                if choice.isdigit() and 1 <= int(choice) <= len(tasks):
                    task_number = int(choice) - 1
                    new_task_name  = input("Enter the new task name: ")
                    tasks[task_number]["task"] = new_task_name
                    save_tasks(tasks)
                    print(f"Task {task_number + 1} updated successfully.")            
                else: print("Invalid task number.")
            elif choice == '2':
                choice = input("Enter your tasks number: ")
                if choice.isdigit() and 1 <= int(choice) <= len(tasks):
                    task_number = int(choice) - 1
                    status_input  = input("Is the task completed? (y/n): ")
                    if status_input.lower() == 'y':
                        tasks[task_number]["done"] = True
                    elif status_input.lower() == 'n':
                        tasks[task_number]["done"] = False
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        continue
                    save_tasks(tasks)
                    print(f"Task {task_number + 1} updated successfully.")

def marks_tasks():
    print("Mark All Tasks:")
    while True:
        print("1. Mark all as DONE")
        print("2. Mark all as NOT DONE")
        print("3. Cancel")
        choice = input("Choose an option:")
        if choice == '1':
            # Mark all tasks as done
            update_all_tasks(True)
            print("All tasks marked as done.\n")
        elif choice == '2':
            # Mark all tasks as not done
            update_all_tasks(False)
            print("All tasks marked as not done.\n")
        elif choice == '3':
            print("Cancelling...")
            return
        else:
            print("Invalid choice.\n")
def delete_tasks():
    while True:
        print("\nDelete Tasks")
        print("1. Delete a specific task")
        print("2. Delete all tasks")
        print("3. Cancel")
        choice = input("Choose an option: ")
        if choice not in ['1','2','3']:
            print("Give choice in number")
        if choice == '3':
            print("Cancelling...")
            return
        elif choice == '1': # delete specific tasks
            tasks = load_tasks()
            if tasks:
                print("Tasks:")
                print("Select the task number to delete:")
                display_tasks(tasks)
                choice = input("Enter task number to delete: ")
                if choice.isdigit() and 1<= int(choice) <=len(tasks):
                    task_number = int(choice) -1
                    confirm_choice = input("Do you want to delete this task y or n: ")
                    if confirm_choice.lower() == 'y':
                        tasks.pop(task_number) 
                        save_tasks(tasks)
                        print("Task deleted.")
                    else:
                        print("Cancelled.")
            else:
                print("No tasks found.")
                return
        elif choice == '2': # delete all the tasks
            tasks = []
            save_tasks(tasks)
            print("All tasks deleted.")
            break

            

def start():
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark All Tasks")
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
            marks_tasks()    
        elif choice == '6':
            print("Thanks for using the To-Do App. See you again!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    start()