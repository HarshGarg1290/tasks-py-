import json

def add_task(tasks):
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task = {"name": task_name, "description": task_description, "completed": False}
    tasks.append(task)
    print("Task added successfully.")

def edit_task(tasks):
    task_index = int(input("Enter task index to edit: "))
    task_name = input("Enter new task name: ")
    task_description = input("Enter new task description: ")
    tasks[task_index]["name"] = task_name
    tasks[task_index]["description"] = task_description
    print("Task edited successfully.")

def delete_task(tasks):
    task_index = int(input("Enter task index to delete: "))
    del tasks[task_index-1]
    print("Task deleted successfully.")

def mark_task_completed(tasks):
    task_index = int(input("Enter task index to mark as completed: "))
    tasks[task_index-1]["completed"] = True
    print("Task marked as completed.")

def mark_task_incomplete(tasks):
    task_index = int(input("Enter task index to mark as incomplete: "))
    tasks[task_index-1]["completed"] = False
    print("Task marked as incomplete.")

def show_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i+1}. {task['name']} - {task['description']} - {status}")

def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def main():
    tasks = load_tasks_from_file()
    while True:
        print("""
        1. Add task
        2. Edit task
        3. Delete task
        4. Mark task as completed
        5. Mark task as incomplete
        6. Show tasks
        7. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
            save_tasks_to_file(tasks)
        elif choice == "2":
            edit_task(tasks)
            save_tasks_to_file(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks_to_file(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
            save_tasks_to_file(tasks)
        elif choice == "5":
            mark_task_incomplete(tasks)
            save_tasks_to_file(tasks)
        elif choice == "6":
            show_tasks(tasks)
        elif choice == "7":
            save_tasks_to_file(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        
        s=input("Return to main menu? Y/N")
        if s=="Y" or s=="y":
            continue
        else:
            print("Goodbye!")
            break
        
        print("-----------------------------------------------------------------------")

if __name__ == "__main__":
    main()