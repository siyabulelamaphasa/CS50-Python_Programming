price_value = 50
avarage_paid = 0
accepted_coins = [25, 10, 5]

while price_value > 0:
    print(f"Amount Due: {price_value}")
    payment = int(input("Insert Coin: "))
    if payment in accepted_coins:

        price_value = price_value - payment
        avarage_paid = avarage_paid + payment

if avarage_paid >= price_value:
    print(f"Change Owed: {avarage_paid - 50}")
