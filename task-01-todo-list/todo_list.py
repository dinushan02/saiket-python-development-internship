tasks = []

def display_menu():
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")


def add_task(tasks):
    description = input("Enter the description: ").strip()

    if not description:
        print("Task description cannot be empty.")
    else:
        task = {
            "description": description,
            "completed": False
        }

        tasks.append(task)

        print("Task added successfully!")


def get_status_label(task):
    if task["completed"]:
        return "Completed"
    else:
        return "Not Completed"


def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n===== YOUR TASKS =====")

        for index, task in enumerate(tasks, start=1):
            status_label = get_status_label(task)
            print(f'{index}. {task["description"]} [{status_label}]')


def view_task(tasks):
    show_tasks(tasks)


def mark_task_completed(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        show_tasks(tasks)

        try:
            task_number = int(input("\nWhich task do you want to mark as complete: "))

            task_index = task_number - 1

            if 0 <= task_index < len(tasks):
                if tasks[task_index]["completed"]:
                    print("This task is already completed.")
                else:
                    tasks[task_index]["completed"] = True
                    print(f"Task '{tasks[task_index]['description']}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    display_menu()

    try:
        user_choice = int(input("\nEnter your choice: "))

        if user_choice < 1 or user_choice > 4:
            print("Please enter the correct choice(1/2/3/4)!")
        elif user_choice == 1:
            add_task(tasks)
        elif user_choice == 2:
            view_task(tasks)
        elif user_choice == 3:
            mark_task_completed(tasks)
        elif user_choice == 4:
            print("Thank you for using the To-Do List!")
            break
    except ValueError:
        print("Invalid choice!")
