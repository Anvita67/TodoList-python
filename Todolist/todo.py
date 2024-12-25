def to_do_list():
    tasks = []

    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed!")
            else:
                print("Task not found!")
        elif choice == '3':
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

to_do_list()
1
