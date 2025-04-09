import requests

def currency_converter():
    # API endpoint (using a free API - exchangeratesapi.io)
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        # Fetch exchange rates
        response = requests.get(url)
        data = response.json()
        rates = data['rates']
        
        # Display available currencies
        print("Available currencies:", ", ".join(rates.keys()))
        
        # Get user input
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()
        
        # Validate currencies
        if from_currency not in rates or to_currency not in rates:
            print("Invalid currency code!")
            return
        
        # Convert amount to USD first (if not already in USD)
        if from_currency != "USD":
            amount_in_usd = amount / rates[from_currency]
        else:
            amount_in_usd = amount
            
        # Convert from USD to target currency
        converted_amount = amount_in_usd * rates[to_currency]
        
        # Display result
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(f"Exchange rate: 1 {from_currency} = {(rates[to_currency]/rates[from_currency]):.4f} {to_currency}")
        
    except requests.RequestException:
        print("Error fetching exchange rates. Please check your internet connection.")
    except ValueError:
        print("Please enter a valid number for the amount.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the converter
if __name__ == "__main__":
    print("Welcome to Currency Converter!")
    currency_converter()