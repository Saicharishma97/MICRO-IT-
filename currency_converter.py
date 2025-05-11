exchange_rates = {
    "USD": {"INR": 82.75, "EUR": 0.93, "GBP": 0.76},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0092},
    "EUR": {"USD": 1.08, "INR": 88.23, "GBP": 0.82},
    "GBP": {"USD": 1.32, "INR": 90.25, "EUR": 1.22},
}

def get_exchange_rate(from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return exchange_rates[from_currency][to_currency]
    else:
        print(f"Error: Exchange rate from {from_currency} to {to_currency} not available.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return amount * rate
    else:
        return None

def main():
    print("Welcome to the Real-Time Currency Converter 🌍💱")
    
    from_curr = input("Enter FROM currency code (e.g., USD): ").upper()
    to_curr = input("Enter TO currency code (e.g., INR): ").upper()

    try:
        amount = float(input(f"Enter amount in {from_curr}: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    result = convert_currency(amount, from_curr, to_curr)
    if result is not None:
        print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}")
    else:
        print("Error fetching exchange rate. Please try again.")

if __name__ == "__main__":
    main()
