import random
import datetime

# Main function to run the crypto trading platform
def main():
    print("Welcome to the Cryptocurrency Trading Platform!")
    portfolio = {}
    history = []

    while True:
        action = input("Choose an action (buy, sell, check portfolio, history, exit): ").lower()
        if action == "buy":
            buy_crypto(portfolio, history)
        elif action == "sell":
            sell_crypto(portfolio, history)
        elif action == "check portfolio":
            check_portfolio(portfolio)
        elif action == "history":
            view_history(history)
        elif action == "exit":
            print("Exiting the platform.")
            break
        else:
            print("Invalid action. Please choose again.")

# Function to simulate buying a cryptocurrency
def buy_crypto(portfolio, history):
    crypto = input("Enter the cryptocurrency symbol you want to buy (e.g., BTC, ETH): ").upper()
    price = get_crypto_price(crypto)

    if price:
        amount = float(input(f"How many units of {crypto} would you like to buy at ${price:.2f} per unit? "))
        portfolio[crypto] = portfolio.get(crypto, 0) + amount
        history.append({
            'action': 'buy',
            'crypto': crypto,
            'amount': amount,
            'price': price,
            'date': datetime.datetime.now()
        })
        print(f"Bought {amount} units of {crypto}.")
    else:
        print(f"Sorry, the cryptocurrency {crypto} is not available.")

# Function to simulate selling a cryptocurrency
def sell_crypto(portfolio, history):
    crypto = input("Enter the cryptocurrency symbol you want to sell: ").upper()

    if crypto in portfolio and portfolio[crypto] > 0:
        price = get_crypto_price(crypto)
        amount = float(input(f"How many units of {crypto} would you like to sell? "))

        if amount <= portfolio[crypto]:
            portfolio[crypto] -= amount
            history.append({
                'action': 'sell',
                'crypto': crypto,
                'amount': amount,
                'price': price,
                'date': datetime.datetime.now()
            })
            print(f"Sold {amount} units of {crypto}.")
        else:
            print(f"You don't have that many units of {crypto} to sell.")
    else:
        print(f"You don't own any units of {crypto}.")

# Function to check the user's portfolio
def check_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        print("Your cryptocurrency portfolio:")
        for crypto, amount in portfolio.items():
            print(f"{crypto}: {amount:.4f} units")

# Function to view transaction history
def view_history(history):
    if not history:
        print("No trading history available.")
    else:
        for record in history:
            print(f"{record['date'].strftime('%Y-%m-%d %H:%M:%S')} - {record['action']} {record['amount']:.4f} units of {record['crypto']} at ${record['price']:.2f}")

# Function to get a simulated cryptocurrency price
def get_crypto_price(crypto):
    crypto_prices = {
        'BTC': random.uniform(30000, 60000),
        'ETH': random.uniform(1500, 4000),
        'LTC': random.uniform(100, 300),
        'XRP': random.uniform(0.5, 2)
        
    }
    return crypto_prices.get(crypto)

if __name__ == "__main__":
    main()
