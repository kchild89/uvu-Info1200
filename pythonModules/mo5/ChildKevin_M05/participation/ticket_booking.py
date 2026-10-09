# Kevin Child - Ticket Booking App

# Define a function that requests and validates a ticket price within the supplied limits.
def get_ticket_price(prompt, low, high):
    # Keep asking until a valid ticket price is returned.
    while True:
        # Attempt to read and convert the input, watching for a conversion error.
        try:
            # Display the prompt and convert the response to a decimal number.
            price = float(input(prompt))
            # Check that the price is greater than the lower limit and no more than the upper limit.
            if low < price <= high:
                # Return the valid ticket price to the caller.
                return price
            # Otherwise, handle a price outside the allowed limits.
            else:
                # Display a message showing the price limits.
                print(f"Enter a price between {low} and {high}.")
        # Handle input that cannot be converted to a decimal number.
        except ValueError:
            # Tell the user to enter a valid number.
            print("Enter a valid number.")


# Define a function that requests and validates a whole number of tickets within the supplied limits.
def get_ticket_count(prompt, low, high):
    # Keep asking until a valid ticket count is returned.
    while True:
        # Attempt to read and convert the input, watching for a conversion error.
        try:
            # Display the prompt and convert the response to an integer.
            count = int(input(prompt))
            # Check that the count is greater than the lower limit and no more than the upper limit.
            if low < count <= high:
                # Return the valid ticket count to the caller.
                return count
            # Otherwise, handle a ticket count outside the allowed limits.
            else:
                # Display a message showing the ticket count limits.
                print(f"Enter a ticket count between {low} and {high}.")
        # Handle input that cannot be converted to an integer.
        except ValueError:
            # Tell the user to enter a valid integer.
            print("Enter a valid integer.")


# Define the main steps of the ticket booking program.
def main():
    # Display the application title.
    print("Kevin Child's Ticket Booking App")
    # Display a blank line.
    print()

    # Ask for and store a ticket price greater than 0 and no more than 200.
    price = get_ticket_price("Enter ticket price: ", 0, 200)
    # Ask for and store a whole number of tickets greater than 0 and no more than 10.
    count = get_ticket_count("Enter number of tickets: ", 0, 10)

    # Multiply the ticket price by the ticket count to calculate the total cost.
    total = price * count

    # Display a blank line.
    print()
    # Display the total cost as dollars with two decimal places.
    print(f"Total price: ${total:.2f}")


# Run the main steps only when this file is executed directly.
if __name__ == "__main__":
    # Call the main function to start the program.
    main()