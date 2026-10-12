# Task 1: To-Do List Application

## Project Overview

The **To-Do List Application** is a command-line application developed using Python as part of my Python Development Internship at **SaiKet Systems**.

The application helps users manage their daily tasks by allowing them to add new tasks, view their task list, and mark tasks as completed. It also includes input validation and exception handling to manage invalid user inputs.

This project demonstrates my understanding of Python fundamentals, including lists, dictionaries, functions, conditional statements, loops, and exception handling.

## Features

- **Add Tasks:** Add new tasks using a task description.
- **View Tasks:** Display all tasks with their task numbers and completion statuses.
- **Mark Tasks as Completed:** Select a task by its number and update its status.
- **Task Status Tracking:** Display whether each task is completed or not completed.
- **Empty Task Validation:** Prevent users from adding empty task descriptions.
- **Input Validation:** Handle invalid menu choices and task numbers.
- **Exception Handling:** Handle non-numeric inputs without terminating the application unexpectedly.
- **Duplicate Completion Prevention:** Inform users when they attempt to complete an already completed task.
- **Interactive Menu:** Continue using the application until the user chooses to exit.

## Technologies Used

- **Programming Language:** Python
- **Application Type:** Command-Line Interface (CLI)
- **Core Concepts:** Lists, dictionaries, functions, loops, conditional statements, indexing, and exception handling

## Project Structure

```text
task-01-todo-list/
├── README.md
└── todo_list.py
```

## Requirements

- Python 3.x
- A code editor or terminal to run the program

No external Python packages are required.

## How to Run the Application

### 1. Clone the Repository

If you have not already cloned the main internship repository, run:

```bash
git clone <your-repository-url>
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Navigate to the Task Folder

```bash
cd saiket-python-development-internship/task-01-todo-list
```

Adjust the folder path if your main repository uses a different name.

### 3. Run the Python File

```bash
python todo_list.py
```

If your system uses the `python3` command, run:

```bash
python3 todo_list.py
```

## How to Use the Application

When the program starts, the following menu is displayed:

```text
===== TO-DO LIST APPLICATION =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit
```

### Example: Adding and Viewing Tasks

Add two tasks:

```text
Enter your choice: 1
Enter the description: Learn Python
Task added successfully!
```

```text
Enter your choice: 1
Enter the description: Read a book
Task added successfully!
```

Select option `2` to view the tasks:

```text
===== YOUR TASKS =====
1. Learn Python [Not Completed]
2. Read a book [Not Completed]
```

### Example: Marking a Task as Completed

Select option `3` and enter the task number:

```text
Which task do you want to mark as complete: 1
Task 'Learn Python' marked as completed!
```

View the updated task list:

```text
===== YOUR TASKS =====
1. Learn Python [Completed]
2. Read a book [Not Completed]
```

### Example: Exiting the Application

Select option `4`:

```text
Thank you for using the To-Do List!
```

## Testing and Validation

The application was tested using the following scenarios to check normal functionality, input validation, and error handling.

| No. | Test Case | Expected Result | Status |
|---:|---|---|---|
| 1 | View tasks before adding any tasks | Display `No tasks found.` | Passed |
| 2 | Add a task with a valid description | Display a success message | Passed |
| 3 | Add two tasks and view the task list | Display both tasks with their numbers and statuses | Passed |
| 4 | Mark an incomplete task as completed | Update its status to `Completed` and display a success message | Passed |
| 5 | View tasks after completing a task | Show the completed task with the correct status | Passed |
| 6 | Try to complete an already completed task | Display `This task is already completed.` | Passed |
| 7 | Enter a non-numeric menu choice, such as `ddd` | Display `Invalid choice!` | Passed |
| 8 | Enter an invalid task number, such as `5`, when only two tasks exist | Display `Invalid task number.` | Passed |
| 9 | Submit an empty task description | Display `Task description cannot be empty.` | Passed |

### Additional Test Cases

The following cases should also be checked to strengthen the application's validation.

| No. | Test Case | Expected Result |
|---:|---|---|
| 10 | Enter a non-numeric value when selecting a task to complete | Display `Please enter a valid number.` |
| 11 | Enter a task number of `0` | Display `Invalid task number.` |
| 12 | Enter a negative task number | Display `Invalid task number.` |
| 13 | Try to mark a task as completed when no tasks exist | Display `No tasks found.` |
| 14 | Enter a description containing only spaces | Display `Task description cannot be empty.` |
| 15 | Enter a menu number outside the range `1–4` | Display `Please enter the correct choice(1/2/3/4)!` |
| 16 | Exit the application using menu option `4` | Display the exit message and terminate the menu loop |

**Testing note:** Test cases 1–9 were demonstrated in the screenshots provided during development. Test cases 10–16 are additional validation scenarios; mark them as passed only after testing them yourself.

## Python Concepts Learned

- **Lists:** Store multiple tasks in a single collection.
- **Dictionaries:** Represent each task using its description and completion status.
- **Functions:** Separate the application's operations into reusable functions.
- **Loops:** Keep the menu running until the user exits.
- **Conditional Statements:** Check menu choices, task statuses, and input validity.
- **`enumerate()`:** Display task numbers starting from 1.
- **List Indexing:** Access and update the selected task.
- **`try` and `except`:** Handle invalid numeric conversions using `ValueError`.
- **String Methods:** Use `.strip()` to remove leading and trailing whitespace from task descriptions.

## Current Limitations

- Tasks are stored in memory and are lost when the application exits.
- The application does not currently save tasks to a file or database.
- The interface is terminal-based and does not include a graphical user interface.
- Tasks do not currently have due dates, priorities, or categories.

These limitations provide opportunities for future improvements.

## Future Improvements

- Save and load tasks using file handling.
- Add task deletion functionality.
- Add task editing functionality.
- Introduce task priorities and due dates.
- Build a graphical interface or web-based version.
- Add automated tests using Python's `unittest` framework.

## What This Project Demonstrates

This project demonstrates the practical application of Python programming fundamentals to build an interactive command-line tool. It emphasizes structured code, task management, input validation, and exception handling.

## Internship Information

**Organization:** SaiKet Systems  
**Internship:** Python Development Internship  
**Task:** Task 1 — To-Do List Application  
**Language:** Python

---

*Built as part of my journey toward becoming a Python Developer.*