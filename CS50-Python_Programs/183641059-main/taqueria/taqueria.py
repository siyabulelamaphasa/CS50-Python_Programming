def main():
    # Define the menu items and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    print("Welcome to Felipe’s Taqueria! Please enter your items one per line.")
    print("Press Control-D (or Control-Z on Windows) to finish your order.\n")

    try:
        while True:
            # Prompt the user for an item
            item = input("Enter an item: ").strip()

            # Check for valid menu items (case insensitive)
            item_titlecased = item.title()  # Convert input to title case
            if item_titlecased in menu:
                total_cost += menu[item_titlecased]
                print(f"Total cost: ${total_cost:.2f}")
            else:
                print("Item not recognized. Please enter a valid menu item.")
    except EOFError:
        # Handle the end of input
        print("\nThank you for your order!")
        print(f"Final total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
