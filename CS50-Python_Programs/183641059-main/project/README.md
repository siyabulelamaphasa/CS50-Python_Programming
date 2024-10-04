# Cryptocurrency Trading Platform
#### Video Demo: https://youtu.be/CiNmo-ma1t0
#### Description: A Python program that simulates a trading platform for digital currencies (cryptocurrencies).This platform will allow users to buy and sell cryptocurrencies, check their portfolio, and view their transaction history.

TODO:

1: project.py – Main Program with Functions
This script will simulate a cryptocurrency trading environment where users can:

Buy cryptocurrencies at a simulated price.
Sell cryptocurrencies from their portfolio.
Check portfolio to view their holdings and total value.
View transaction history to see previous buy and sell orders.

2: test_project.py – Pytest Tests for Functions
This file will contain unit tests for the main functions using the pytest framework. We'll test:

get_crypto_price function to ensure it returns valid prices.
buy_crypto and sell_crypto functions to ensure they modify the portfolio and history correctly.

3: requirements.txt – List of Dependencies
Include any necessary dependencies for your project. For this simple project, we’ll need pytest for testing:

Explanation of Key Parts:
Main Function: main() serves as the entry point for the cryptocurrency trading platform, guiding the user through different actions (buy, sell, check portfolio, view history, and exit).
Buy Crypto Function: buy_crypto() allows the user to buy cryptocurrencies at simulated prices. It updates the portfolio and logs the transaction in the history.
Sell Crypto Function: sell_crypto() lets users sell cryptocurrencies from their portfolio, deducting the amount sold and logging the transaction in the history.
Check Portfolio Function: check_portfolio() shows the user's current holdings of different cryptocurrencies.
View History Function: view_history() displays the transaction history with details such as the cryptocurrency traded, quantity, price, and timestamp.
Simulated Crypto Prices: get_crypto_price() generates random prices for a few selected cryptocurrencies.
