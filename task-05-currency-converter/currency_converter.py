import requests

try:
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Amount must be greater than zero!")

    else:
        source_currency = input("Enter your source currency (e.g., USD): ").strip().upper()
        target_currency = input("Enter your target currency (e.g., EUR): ").strip().upper()

        if not source_currency or not target_currency:
            print("Currency codes cannot be empty!")

        elif source_currency == target_currency:
            print(f"\nAmount: {amount:.2f}")
            print(f"From: {source_currency}")
            print(f"To: {target_currency}")
            print(f"Converted Amount: {amount:.2f} {target_currency}")

        else:
            url = ("https://api.frankfurter.dev/v1/latest"f"?base={source_currency}&symbols={target_currency}")

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            rates = data.get("rates", {})
            exchange_rate = rates.get(target_currency)

            if exchange_rate is None:
                print("Exchange rate not available for this currency pair.")
            else:
                converted_amount = amount * exchange_rate

                print(f"\nAmount: {amount:.2f}")
                print(f"From: {source_currency}")
                print(f"To: {target_currency}")
                print(f"Converted Amount: {converted_amount:.2f} {target_currency}")

except ValueError:
    print("Please enter a valid numeric amount!")

except requests.exceptions.JSONDecodeError:
    print("The API returned invalid JSON data.")

except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")