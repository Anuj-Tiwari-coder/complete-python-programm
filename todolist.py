# todo.py

# List to store tasks
tasks = []

def show_menu():
    print("\nTo-Do List:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def delete_task():
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def mark_completed():
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task '{tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Exiting To-Do List!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
