Tickets = {
    "Interstellar": 300,
    "Taxi Driver": 250,
    "Shawshank Redemption": 300,
    "The Batman Begins": 250,
    "Fight Club": 200
}

Foods = {
    "Cheese Popcorn": 150,
    "Caramel Popcorn": 180,
    "Normal Popcorn": 140,
    "Coke": 75,
    "Water": 20
}


def display_details(tickets, foods):
    print("----- Ticket Counter -------")
    for key, value in tickets.items():
        print(f"{key:25} : Rs. {value}")

    print("\n---- Food Counter -----")
    for key, value in foods.items():
        print(f"{key:25} : Rs. {value}")


def add_to_cart(tickets, foods):
    cart = []
    total = 0

    print("\nType 'n' to finish your order.")

    while True:
        user_ask = input("\nEnter item name (Ticket/Food): ").title()

        if user_ask.lower() == "n":
            print("Thank you for buying.\n")
            break

        elif user_ask in tickets:
            total += tickets[user_ask]
            cart.append(user_ask)
            print(f"{user_ask} added to cart")

        elif user_ask in foods:
            total += foods[user_ask]
            cart.append(user_ask)
            print(f"{user_ask} added to cart")

        else:
            print("Item not available.")

    return total, cart


def display(total, cart):
    print("---- YOUR ORDER -----")
    print("Your Purchase list:")
    for item in cart:
        print("-", item)

    print(f"\nYour total is Rs. {total}")


def main():
    display_details(Tickets, Foods)
    total, cart = add_to_cart(Tickets, Foods)
    display(total, cart)


main()
