# Task 6: Word Count Tool

## 📌 Project Overview

The **Word Count Tool** is a Python-based program developed as part of the SaiKet Systems Python Development Internship. It reads a text file and analyzes its contents by calculating the total number of words, lines, and characters. It also performs word frequency analysis to identify the most commonly used words in the text.

This project demonstrates practical knowledge of Python file handling, string manipulation, data analysis, and exception handling.

## 🎯 Objectives

- Read and analyze text from a file.
- Count the total number of words, lines, and characters.
- Identify the frequency of individual words.
- Display the complete word frequency distribution.
- Identify the top five most common words.
- Handle empty files and missing files appropriately.

## ✨ Features

- **File Input:** Reads text from `sample.txt` using UTF-8 encoding.
- **Word Count:** Calculates the total number of words using whitespace-based splitting.
- **Line Count:** Counts the lines returned by Python's `splitlines()` method.
- **Character Count:** Counts every character in the original file content, including letters, digits, spaces, punctuation, and newline characters.
- **Case-Insensitive Analysis:** Converts text to lowercase so words with different capitalization are counted together.
- **Punctuation Removal:** Removes standard punctuation before calculating word frequencies.
- **Complete Word Frequency Distribution:** Displays each word and its frequency.
- **Top Five Common Words:** Displays the five most frequently occurring words, or fewer if the text contains fewer than five unique words.
- **Empty-File Handling:** Detects files containing no text or only whitespace.
- **Error Handling:** Displays a helpful message if `sample.txt` cannot be found.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Module:** `collections.Counter`
- **Module:** `string`
- **Concepts:** File Input/Output, String Manipulation, Data Analysis, Loops, Conditional Statements, and Exception Handling

## 📂 Project Structure

```text
task-06-word-count-tool/
├── word_count.py
├── sample.txt
└── README.md
```

## ⚙️ Requirements

- Python 3.x
- No external package installation is required. The program uses Python's standard library.

## 🚀 How to Run

### Step 1: Open the project folder

Open the `task-06-word-count-tool` folder in Visual Studio Code.

### Step 2: Prepare the input file

Ensure that `sample.txt` exists in the same directory as `word_count.py` and contains the text you want to analyze.

### Step 3: Run the program

Open the terminal in the project directory and execute:

```bash
python word_count.py
```

If your system uses the Python launcher, you can also run:

```bash
py word_count.py
```

### Step 4: Review the results

The program displays:

1. File-reading status.
2. Total word count.
3. Total line count.
4. Total character count.
5. Complete word frequency distribution.
6. Top five most common words.

## 🧪 Testing

The following test cases can be used to verify the program.

| Test Case | Procedure | Expected Result |
|---|---|---|
| Normal file | Run with text in `sample.txt`. | Displays counts and word frequencies. |
| Empty file | Remove all content from `sample.txt` and save it. | Displays `The file is empty!` |
| Whitespace-only file | Put only spaces or blank lines in the file. | Displays `The file is empty!` |
| Missing file | Temporarily rename or move `sample.txt`. | Displays `The file was not found.` |
| Case-insensitive counting | Include `Python`, `python`, and `PYTHON`. | Counts them together as `python`. |
| Punctuation handling | Include words such as `Python,` and `Python.`. | Removes standard punctuation before frequency counting. |
| Frequency accuracy | Repeat a word several times. | Displays the correct frequency for that word. |

**Note:** Restore the original `sample.txt` after completing the empty-file and missing-file tests.

## 📊 Character Counting Method

The program uses Python's `len(text)` to calculate the character count.

This counts **all characters in the original text**, including:

- Letters and digits
- Spaces between words
- Punctuation marks
- Newline characters

Therefore, the reported character count is not limited to letters or visible characters. Newline characters also contribute to the total.

## 📚 Learning Outcomes

Through this project, I practiced:

- Reading text files using Python's `open()` function.
- Managing files with a `with` statement.
- Counting words, lines, and characters.
- Cleaning text using lowercase conversion and punctuation removal.
- Analyzing word frequencies using `collections.Counter`.
- Handling missing files with `FileNotFoundError`.
- Organizing program output into clear sections.
- Testing programs with normal and edge-case inputs.

## 🔮 Future Improvements

Possible enhancements include:

- Allowing users to enter a file path.
- Ignoring common stop words such as *the*, *is*, and *and* when ranking frequent words.
- Saving analysis results to a separate report file.
- Displaying frequency results in descending order.
- Adding a graphical user interface.

These are potential future enhancements and are not included in the current implementation.

## 👨‍💻 Internship Project

**Program:** Python Development Internship  
**Organization:** SaiKet Systems  
**Task:** Task 6 – Word Count Tool

This project was created for educational purposes to practice Python programming and text-file analysis.