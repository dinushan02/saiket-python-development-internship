# Task 3: Basic File Handling

## Project Overview

The **Basic File Handling** project is developed using Python as part of my Python Development Internship at **SaiKet Systems**.

This project reads text from a file, checks whether a specific word exists, replaces the word with another word, and saves the modified content back to the same file.

It also handles common file-related scenarios, including missing files, empty files, and files that do not contain the target word.

## Features

- **Read File Content:** Reads text from `sample.txt`.
- **Empty File Detection:** Checks whether the file contains any text.
- **Word Search:** Checks whether the word `Python` exists in the file.
- **Find and Replace:** Replaces every occurrence of `Python` with `Java`.
- **Save Modified Content:** Writes the updated content back to `sample.txt`.
- **Word Not Found Handling:** Displays a message when `Python` does not exist in the file.
- **File Not Found Handling:** Catches `FileNotFoundError` and displays a helpful message.
- **Success Message:** Confirms when the modified content has been saved successfully.

## Technologies Used

- **Programming Language:** Python
- **Application Type:** Command-Line Program
- **Core Concepts:** File handling, string manipulation, conditional statements, and exception handling
- **Built-in Functions and Methods:** `open()`, `read()`, `replace()`, and `write()`

## Project Structure

```text
task-03-basic-file-handling/
├── README.md
├── file_handling.py
└── sample.txt
```

## Requirements

- Python 3.x
- A code editor or terminal to run the program

No external Python packages are required.

## How to Run the Program

### 1. Navigate to the Task Folder

Open your terminal in the main internship repository and run:

```bash
cd task-03-basic-file-handling
```

### 2. Prepare the Sample File

Create a file named `sample.txt` in the task folder.

Example content:

```text
Python is easy to learn.
I am learning Python programming.
Python helps me build useful projects.
```

### 3. Run the Python Program

```bash
python file_handling.py
```

If your system uses `python3`, run:

```bash
python3 file_handling.py
```

## How the Program Works

### Step 1: Read the File

The program opens `sample.txt` in read mode and reads its content.

### Step 2: Check Whether the File Is Empty

If the file contains no text, the program displays:

```text
The file is empty!
```

### Step 3: Search for the Target Word

If the file contains text, the program checks whether `Python` appears in the content.

### Step 4: Replace and Save

If the target word is found, the program replaces every occurrence of `Python` with `Java` and writes the modified content back to `sample.txt`.

Example output:

```text
Text replaced and saved successfully!
```

### Step 5: Handle Other Scenarios

If `Python` does not appear in the file, the program displays:

```text
The word 'Python' was not found in the file.
```

If `sample.txt` cannot be found, the program displays:

```text
'sample.txt' was not found.
```

## Example

### Original File Content

```text
Python is easy to learn.
I am learning Python programming.
Python helps me build useful projects.
```

### After Running the Program

```text
Java is easy to learn.
I am learning Java programming.
Java helps me build useful projects.
```

The modified content is saved back to `sample.txt`.

## Testing and Validation

The following test cases cover the scenarios supported by the program.

| No. | Test Case | Expected Result |
|---:|---|---|
| 1 | File contains the word `Python` | Replace all occurrences with `Java` and save the file |
| 2 | File contains multiple occurrences of `Python` | Replace every occurrence with `Java` |
| 3 | File contains text but no `Python` | Display the word-not-found message |
| 4 | File exists but is empty | Display `The file is empty!` |
| 5 | `sample.txt` does not exist | Display the file-not-found message |
| 6 | Run the program again after all occurrences were replaced | Display the word-not-found message if no `Python` remains |

**Testing note:** These cases reflect the program's logic. Mark them as passed after confirming each result by running the program.

## Python Concepts Learned

### 1. File Handling

Used `open()` to access a text file in read and write modes.

### 2. Context Managers

Used the `with open(...)` pattern to ensure files are closed automatically after operations.

### 3. Reading File Content

Used `file.read()` to retrieve the complete text from the file.

### 4. String Manipulation

Used `content.replace("Python", "Java")` to replace all occurrences of the target text.

### 5. Conditional Statements

Used `if` and `else` to check for empty content and determine whether the target word exists.

### 6. Exception Handling

Used `try-except` to handle `FileNotFoundError` gracefully.

### 7. Writing to a File

Used `file.write()` to save the modified content back to the original file.

## Current Limitations

- The program searches for the exact, case-sensitive text `Python`.
- The replacement text is fixed as `Java`.
- The program modifies the original file rather than creating a separate output file.
- The program currently handles `FileNotFoundError`, but not every possible file-related exception.

## Future Improvements

- Allow users to enter the word they want to find and replace.
- Allow users to choose the replacement word.
- Add case-insensitive searching.
- Create a backup before modifying the original file.
- Handle additional file-related errors, such as permission errors.
- Add automated tests using Python's `unittest` framework.

## What This Project Demonstrates

This project demonstrates how Python can be used to read, search, modify, and save text files. It also provides practical experience with string manipulation, conditional logic, and exception handling.

## Internship Information

**Organization:** SaiKet Systems  
**Internship:** Python Development Internship  
**Task:** Task 3 — Basic File Handling  
**Programming Language:** Python

---

*Built as part of my journey toward becoming a Python Developer.*