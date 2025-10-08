tasks = []
while True:
    print("\n--- To-Do Lists ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("-------------------------")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("You have no tasks.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        new_task = input("Enter the task to add: ").strip()
        if new_task:
            tasks.append(new_task)
            print(f"Task '{new_task}' was added.")
        else:
            print("Cannot add an empty task.")

    elif choice == '3':
        print("\n--- Update a Task ---")
        if not tasks:
            print("There are no tasks to update.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_number = int(input("Enter the number of the task to update: "))
                if 1 <= task_number <= len(tasks):
                    updated_task = input("Enter the new task description: ").strip()
                    if updated_task:
                        tasks[task_number - 1] = updated_task
                        print("Task updated successfully.")
                    else:
                        print("Cannot update to an empty task.")
                else:
                    print("That task number does not exist.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == '4':
        print("\n--- Delete a Task ---")
        if not tasks:
            print("There are no tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_to_delete = int(input("Enter the number of the task to delete: "))
                if 1 <= task_to_delete <= len(tasks):
                    removed = tasks.pop(task_to_delete - 1)
                    print(f"Deleted task: '{removed}'")
                else:
                    print("That task number does not exist.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == '5':
        print("Thanks for using the To-Do List application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")