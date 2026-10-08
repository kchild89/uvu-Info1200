# Kevin Child — validation module for the Future Value app

# Define a function that requests and validates a decimal number within the supplied limits.
def get_float(prompt, low, high): 
    # Keep asking until a valid decimal number is returned.
    while True:
        # Attempt to read and convert the input, watching for a conversion error.
        try:
            # Display the prompt and convert the response to a decimal number.
            value = float(input(prompt))
            # Check that the number is greater than the lower limit and no more than the upper limit.
            if low < value <= high:
                # Return the valid decimal number to the caller.
                return value
            # Otherwise, handle a number outside the allowed limits.
            else:
                # Display a message showing the number limits.
                print(f"Enter a number between {low} and {high}.")   
        # Handle input that cannot be converted to a decimal number.
        except ValueError:
            # Tell the user to enter a valid number.
            print("Enter a valid number.")

# Define a function that requests and validates an integer within the supplied limits.
def get_int(prompt, low, high):
    # Keep asking until a valid integer is returned.
    while True:
        # Attempt to read and convert the input, watching for a conversion error.
        try:
            # Display the prompt and convert the response to an integer.
            value = int(input(prompt))
            # Check that the integer is greater than the lower limit and no more than the upper limit.
            if low < value <= high:
                # Return the valid integer to the caller.
                return value
            # Otherwise, handle an integer outside the allowed limits.
            else:
                # Display a message showing the integer limits.
                print(f"Enter an integer between {low} and {high}.")
        # Handle input that cannot be converted to an integer.
        except ValueError:
            # Tell the user to enter a valid number.
            print("Enter a valid number.")

# Define the main steps for trying the validation functions.
def main():
    # Set the starting choice to yes so validation runs at least once.
    choice = "y"
    # Repeat while the user chooses yes, ignoring capitalization.
    while choice.lower() == "y":
        # Ask for and store a decimal number greater than 0 and no more than 1000.
        floatValue = get_float("Enter a number greater than 0 and up to 1000:\t", 0, 1000)
        # Ask for and store an integer greater than 0 and no more than 50.
        intValue = get_int("Enter an integer greater than 0 and up to 50:\t", 0, 50)
        # Display the validated decimal number.
        print(floatValue)
        # Display the validated integer.
        print(intValue)

        # Ask whether the user wants to try again and save the response.
        choice = input("Continue? (y/n): ")
        # Display a blank line.
        print()

    # Display a goodbye message after the user stops.
    print("Bye!")
        
# Run the main steps only when this file is executed directly.
if __name__ == "__main__":
    # Call the main function to start the program.
    main()