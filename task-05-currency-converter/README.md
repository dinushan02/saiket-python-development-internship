# Task 5: Currency Converter

A simple, command-line Currency Converter built with Python that converts an amount from one currency to another using exchange-rate data from the [Frankfurter API](https://api.frankfurter.dev/).

This project was developed as **Task 5** of my Python Development Internship at SaiKet Systems.

## 📌 Project Overview

The Currency Converter accepts an amount, a source currency, and a target currency from the user. It retrieves the exchange rate from the API, calculates the converted amount, and displays the result.

The program also includes input validation and error handling to manage invalid amounts, unsupported currencies, and API request failures.

## ✨ Features

- Convert between currencies supported by the Frankfurter API.
- Accept decimal amounts.
- Automatically standardize currency codes to uppercase.
- Validate amounts to ensure they are greater than zero.
- Handle empty currency inputs.
- Convert identical currencies without making an API request.
- Retrieve exchange rates through an API.
- Handle HTTP errors and network failures.
- Handle invalid JSON responses and missing exchange-rate data.
- Display converted amounts to two decimal places.

## 🛠️ Technologies Used

- **Python 3** — Programming language
- **Requests** — HTTP requests and API integration
- **Frankfurter API** — Exchange-rate data

## 📂 Project Structure

```text
task-05-currency-converter/
│
├── currency_converter.py
└── README.md
```

## ⚙️ Installation

### 1. Install Python

Install Python 3 from the official website:

https://www.python.org/downloads/

### 2. Clone the repository

```bash
git clone https://github.com/dinushan02/saiket-python-development-internship.git
```

### 3. Navigate to the project folder

```bash
cd saiket-python-development-internship/task-05-currency-converter
```

### 4. Install the required library

```bash
pip install requests
```

## ▶️ How to Run

Run the following command in your terminal:

```bash
python currency_converter.py
```

Follow the prompts to enter the amount, source currency, and target currency.

## 💻 Example Usage

**Example 1: Successful conversion**

```text
Enter amount: 100
Enter your source currency (e.g., USD): USD
Enter your target currency (e.g., EUR): EUR

Amount: 100.00
From: USD
To: EUR
Converted Amount: 89.33 EUR
```

*Note: This is an illustrative example. Actual results depend on the exchange rate returned by the API.*

**Example 2: Same-currency conversion**

```text
Enter amount: 100
Enter your source currency (e.g., USD): USD
Enter your target currency (e.g., EUR): USD

Amount: 100.00
From: USD
To: USD
Converted Amount: 100.00 USD
```

**Example 3: Invalid amount**

```text
Enter amount: -10
Amount must be greater than zero!
```

**Example 4: Invalid numeric input**

```text
Enter amount: abc
Please enter a valid numeric amount!
```

## 🌐 API Information

This project uses the Frankfurter API to retrieve exchange-rate data.

**API documentation:** https://frankfurter.dev/

Example API endpoint:

```text
https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR
```

The API returns exchange-rate information in JSON format. The program extracts the requested rate and multiplies it by the input amount.

**Currency support:** Only currencies available through the API can be converted. For example, LKR (Sri Lankan Rupee) is not included in the supported-currency list checked during development. An unsupported currency may result in an API error.

## 🛡️ Error Handling

The program includes handling for:

- Non-numeric amounts
- Zero or negative amounts
- Empty currency codes
- HTTP errors
- Network and request failures
- Invalid JSON responses
- Missing exchange-rate data

## 🧪 Testing

The following cases can be used to test the program:

| Test case | Expected behavior |
|---|---|
| USD to EUR | Displays the converted amount |
| EUR to USD | Converts in the reverse direction |
| USD to USD | Returns the original amount |
| Zero amount | Displays an error |
| Negative amount | Displays an error |
| Non-numeric amount | Displays an error |
| Empty currency code | Displays an error |
| Unsupported currency | Handles the API error |
| Network failure | Displays a request-error message |

## 🎯 Learning Outcomes

Through this project, I practiced:

- Integrating a third-party API using Python
- Sending HTTP GET requests
- Working with JSON responses and dictionaries
- Handling user input and validating data
- Performing calculations using exchange rates
- Handling exceptions and API errors
- Organizing and documenting a Python project

## 👨‍💻 Internship

**Organization:** SaiKet Systems  
**Role:** Python Development Intern  
**Project:** Task 5 — Currency Converter

This project was developed as part of my internship learning journey to improve my Python programming, API integration, and error-handling skills.

## 📄 License

This project is intended for educational and learning purposes.