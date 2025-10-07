# This list will store all our tasks.
tasks = []

while True:
    print("\n--- To-Do Lists ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("-------------------------")
    # Get the user's choice
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("You have no tasks.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        # Get the new task from the user
        new_task = input("Enter the task to add: ").strip()
        if new_task:
            # Add the new task to our list
            tasks.append(new_task)
            print(f"Task '{new_task}' was added.")
        else:
            print("Cannot add an empty task.")

    elif choice == '3':
        print("\n--- Update a Task ---")
        if not tasks:
            print("There are no tasks to update.")
        else:
            # Show tasks so the user can pick one
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_number = int(input("Enter the number of the task to update: "))
                # Check if the number is valid
                if 1 <= task_number <= len(tasks):
                    # Get the new task description
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
            # Show tasks so the user can pick one
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                # Ask which task number to delete
                task_to_delete = int(input("Enter the number of the task to delete: "))
                # Check if the number is valid
                if 1 <= task_to_delete <= len(tasks):
                    removed = tasks.pop(task_to_delete - 1)
                    print(f"Deleted task: '{removed}'")
                else:
                    print("That task number does not exist.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == '5':
        # Exit the application
        print("Thanks for using the To-Do List application. Goodbye!")
        break

    else:
        # Handle cases where the user enters something other than 1-5
        print("Invalid choice. Please enter a number from 1 to 5.")
# This is a simple command-line to-do list application.