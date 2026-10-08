# Kevin Child - Ticket Booking App

def get_ticket_price(prompt, low, high):
    while True:
        try:
            price = float(input(prompt))
            if low < price <= high:
                return price
            else:
                print(f"Enter a price between {low} and {high}.")
        except ValueError:
            print("Enter a valid number.")


def get_ticket_count(prompt, low, high):
    while True:
        try:
            count = int(input(prompt))
            if low < count <= high:
                return count
            else:
                print(f"Enter a ticket count between {low} and {high}.")
        except ValueError:
            print("Enter a valid integer.")


def main():
    print("Kevin Child's Ticket Booking App")
    print()

    price = get_ticket_price("Enter ticket price: ", 0, 200)
    count = get_ticket_count("Enter number of tickets: ", 0, 10)

    total = price * count

    print()
    print(f"Total price: ${total:.2f}")


if __name__ == "__main__":
    main()