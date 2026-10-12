# Task 2: Number Guessing Game

## Project Overview

The **Number Guessing Game** is a command-line application developed using Python as part of my Python Development Internship at **SaiKet Systems**.

In this game, the program generates a random secret number between 1 and 100. The user attempts to guess the number, and the program provides hints to indicate whether each valid guess is too high or too low.

The game continues until the user guesses the correct number. It also tracks the number of valid guesses and handles invalid user input.

## Features

- **Random Number Generation:** Generates a secret number between 1 and 100.
- **Interactive Gameplay:** Allows users to enter guesses through the terminal.
- **Higher and Lower Hints:** Provides feedback when a guess is too high or too low.
- **Attempt Counter:** Counts valid guesses, including the correct guess.
- **Input Validation:** Rejects numbers outside the range of 1 to 100.
- **Exception Handling:** Handles non-numeric input without terminating the game unexpectedly.
- **Clear Feedback:** Displays messages for invalid inputs and incorrect guesses.
- **Winning Message:** Congratulates the user when the correct number is guessed.
- **Singular and Plural Grammar:** Displays `attempt` for one guess and `attempts` for multiple guesses.

## Technologies Used

- **Programming Language:** Python
- **Application Type:** Command-Line Interface (CLI)
- **Python Module:** `random`
- **Core Concepts:** Variables, loops, conditional statements, exception handling, user input, and counters

## Project Structure

```text
task-02-number-guessing-game/
├── README.md
└── number_guessing_game.py
```

## Requirements

- Python 3.x
- A code editor or terminal to run the program

The project uses Python's built-in `random` module. No external packages are required.

## How to Run the Application

### 1. Clone the Repository

If you have not already cloned the main internship repository, run:

```bash
git clone <your-repository-url>
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Navigate to the Task Folder

```bash
cd saiket-python-development-internship/task-02-number-guessing-game
```

Adjust the path if your main repository uses a different name.

### 3. Run the Python Program

```bash
python number_guessing_game.py
```

If your system uses `python3`, run:

```bash
python3 number_guessing_game.py
```

## How to Play

### Step 1: Start the Game

When the program starts, it displays a welcome message:

```text
Welcome to Number Guessing Game!
```

### Step 2: Enter a Guess

The program asks the user to enter a number:

```text
Guess a number:
```

Enter a whole number between 1 and 100.

### Step 3: Follow the Hints

If the guess is lower than the secret number, the program displays:

```text
Too low! Try again.
```

If the guess is higher than the secret number, the program displays:

```text
Too high! Try again.
```

### Step 4: Guess the Correct Number

When the correct number is entered, the program displays a congratulatory message with the number of valid guesses.

Example:

```text
Congratulations 🎉 You guessed the number in 4 attempts.
```

The number shown above is an illustrative example. The actual result depends on the generated secret number and the user's guesses.

## Input Validation and Error Handling

The application checks user input to keep the game running correctly.

### Numbers Outside the Allowed Range

If the user enters a number below 1 or above 100, the program displays:

```text
Please guess a number between 1 and 100.
```

The invalid guess does not increase the attempt counter.

### Non-Numeric Input

If the user enters text such as `abc`, the program displays:

```text
Please enter a valid whole number!
```

The application catches the `ValueError` raised when converting invalid text to an integer and allows the user to try again.

### Decimal Input

If the user enters a decimal such as `12.5`, the integer conversion raises a `ValueError`, and the application displays the validation message.

## Testing and Validation

The following test cases can be used to verify the application's behavior.

| No. | Test Case | Expected Result |
|---:|---|---|
| 1 | Start the application | Display the welcome message |
| 2 | Enter a valid guess lower than the secret number | Display `Too low! Try again.` |
| 3 | Enter a valid guess higher than the secret number | Display `Too high! Try again.` |
| 4 | Guess the correct secret number | Display a congratulatory message and the valid attempt count |
| 5 | Enter `0` | Reject the guess and display the range validation message |
| 6 | Enter `101` | Reject the guess and display the range validation message |
| 7 | Enter `abc` | Display the whole-number validation message and continue |
| 8 | Enter `12.5` | Display the whole-number validation message and continue |
| 9 | Enter an invalid guess followed by a valid guess | Count only valid guesses within the range |
| 10 | Guess the correct number on the first valid attempt | Display `1 attempt` |
| 11 | Guess the correct number after several valid attempts | Display the correct total using `attempts` |
| 12 | Enter multiple incorrect valid guesses before winning | Continue providing hints until the correct number is guessed |

**Testing note:** Mark these test cases as passed only after running the program and confirming the actual results.

## Python Concepts Learned

### 1. Importing a Module

The `random` module is imported to generate a random integer.

### 2. Variables

Variables store the secret number, the user's guess, and the number of valid attempts.

### 3. Loops

A `while` loop allows the game to continue until the correct number is guessed.

### 4. Conditional Statements

`if`, `elif`, and `else` statements compare the guess with the secret number and determine the appropriate feedback.

### 5. Input Validation

Conditional statements check whether a guess falls within the permitted range.

### 6. Exception Handling

A `try-except` block handles invalid input that cannot be converted to an integer.

### 7. Attempt Counting

A counter tracks valid guesses and includes the winning guess in the final total.

### 8. String Formatting

An f-string displays the attempt count and the appropriate singular or plural form of the word `attempt`.

### 9. Loop Control

The `continue` statement skips invalid out-of-range guesses, while `break` ends the game after a correct guess.

## Current Limitations

- The game uses a fixed range from 1 to 100.
- The secret number is not displayed before the game ends.
- The game does not currently provide a maximum attempt limit.
- The game does not currently offer difficulty levels.
- The game does not save game history or scores.

## Future Improvements

- Add easy, medium, and hard difficulty levels.
- Allow users to choose the number range.
- Introduce a maximum number of attempts.
- Add a replay option.
- Track the best score across games.
- Create a graphical user interface.

## What This Project Demonstrates

This project demonstrates how Python programming fundamentals can be used to create an interactive guessing game. It provides practical experience with random number generation, loops, conditional logic, input validation, exception handling, and attempt counting.

## Internship Information

**Organization:** SaiKet Systems  
**Internship:** Python Development Internship  
**Task:** Task 2 — Number Guessing Game  
**Programming Language:** Python

---

*Built as part of my journey toward becoming a Python Developer.*