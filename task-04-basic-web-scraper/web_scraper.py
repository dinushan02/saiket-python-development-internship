import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")

        for book in books:
            title_element = book.select_one("h3 a")

            if title_element:
                title = title_element["title"]
            else:
                title = "Title not available"

            price_element = book.select_one(".price_color")

            if price_element:
                price = price_element.get_text(strip=True)
                price = price.replace("Â", "")
            else:
                price = "Price not available"

            print(f"Book: {title}")
            print(f"Price: {price}")
            print("------------------------------\n")

    else:
        print(f"Failed to retrieve webpage. {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"The request failed! {error}")