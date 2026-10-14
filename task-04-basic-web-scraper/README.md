# Task 4: Basic Web Scraper

## Overview

This project is part of my Python Development Internship at SaiKet Systems. It demonstrates the fundamentals of web scraping using Python to extract book titles and prices from the Books to Scrape demo website.

## Features

- Retrieves webpage content using the Requests library.
- Parses HTML content using Beautiful Soup.
- Extracts book titles and prices from product elements.
- Handles missing book titles and prices with fallback messages.
- Checks the HTTP response status code.
- Handles request-related exceptions.
- Displays extracted book information in a readable format.

## Technologies Used

- **Programming Language:** Python
- **HTTP Requests:** Requests
- **HTML Parsing:** Beautiful Soup 4
- **Data Selection:** CSS selectors

## Project Structure

```text
task-04-basic-web-scraper/
├── web_scraper.py
└── README.md
```

## Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install requests beautifulsoup4
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal inside the project folder.
3. Install the required libraries if they are not already installed.
4. Run the Python script using:

```bash
python web_scraper.py
```

## How It Works

1. Defines the URL of the Books to Scrape website.
2. Sends an HTTP GET request using the Requests library with a timeout.
3. Checks whether the response status code is `200`.
4. Parses the webpage HTML using Beautiful Soup and `html.parser`.
5. Selects book containers using the CSS selector `article.product_pod`.
6. Extracts each book's title from the `title` attribute of the `h3 a` element.
7. Extracts the price from the `.price_color` element.
8. Handles missing title or price elements with fallback messages.
9. Removes the unwanted `Â` character from the extracted price when present.
10. Prints each book's title and price in the terminal.
11. Handles request-related exceptions and displays an error message when a request fails.

## Sample Output

```text
Book: A Light in the Attic
Price: £51.77
------------------------------

Book: Tipping the Velvet
Price: £53.74
------------------------------

Book: Soumission
Price: £50.10
------------------------------
```

*The output shown is an example. Actual results depend on the webpage content.*

## Error Handling

The program includes the following checks:

- **HTTP status check:** Displays a failure message when the response status code is not `200`.
- **Missing title:** Displays `Title not available` if the title element is missing.
- **Missing price:** Displays `Price not available` if the price element is missing.
- **Request exceptions:** Catches `requests.exceptions.RequestException` and displays the error message.

## Limitations

- The scraper currently extracts books from the first catalogue page only.
- Pagination is not implemented.
- CSV export and database storage are not implemented.
- The scraper depends on the website's HTML structure.
- Missing title and price elements are handled, but other unexpected parsing errors are not explicitly handled.

## Concepts Learned

- Sending HTTP GET requests with Python.
- Understanding HTTP response status codes.
- Parsing HTML documents.
- Using CSS selectors with Beautiful Soup.
- Extracting text and HTML attributes.
- Working with lists of HTML elements.
- Using loops and conditional statements.
- Handling request-related exceptions.
- Displaying structured information in the terminal.

## Future Improvements

- Add pagination to scrape multiple catalogue pages.
- Export extracted book information to a CSV file.
- Store scraped data in a database.
- Improve handling of unexpected HTML structures.
- Organize the extracted data into a more structured format.

## Internship Information

- **Organization:** SaiKet Systems
- **Internship:** Python Development Internship
- **Task:** Task 4 – Basic Web Scraper

## Author

Developed as part of my Python Development Internship learning journey.