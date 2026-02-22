# To-Do List with Completion Status (Multiple Add Option)

todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Multiple Tasks")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nEnter your tasks one by one.")
        print("Type 'done' when finished.\n")

        while True:
            task = input("Enter task: ")
            if task.lower() == "done":
                break
            todo_list.append({"task": task, "done": False})

        print("Tasks added successfully!")

    elif choice == "2":
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(todo_list, start=1):
                status = "Completed" if item["done"] else "Pending"
                print(f"{i}. {item['task']} - {status}")

    elif choice == "3":
        if not todo_list:
            print("No tasks available.")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item['task']}")
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                todo_list[task_num - 1]["done"] = True
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item['task']}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = todo_list.pop(task_num - 1)
                print(f"Removed task: {removed['task']}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. \nGoodbye!")
        break

    else:
        print("Invalid choice. Please try again.")