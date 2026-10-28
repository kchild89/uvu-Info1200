#!/usr/bin/env python3

import random  # Import the module used to generate a random number.

def display_title():  # Define a function that displays the game title.
    print("Guess the number!")  # Display the title of the game.
    print()  # Print a blank line for spacing.

def get_limit():  # Define a function that asks for the largest possible number.
    limit = int(input("Enter the upper limit for the range of numbers: "))  # Read the upper limit and convert it to an integer.
    return limit  # Return the upper limit to the caller.

def play_game(limit):  # Define a function that plays one round using the given upper limit.
    number = random.randint(1, limit)  # Choose a random integer from 1 through the upper limit, inclusive.
    count = 0  # Start the guess counter at zero.
    print(f"I'm thinking of a number from 1 to {limit}\n")  # Display the range of possible numbers followed by a blank line.

    while True:  # Keep asking for guesses until the function returns after a correct guess.
        guess = int(input("Your guess: "))  # Read the player's guess and convert it to an integer.
        if guess < number:  # Check whether the guess is smaller than the secret number.
            print("Too low.")  # Tell the player to guess a higher number.
            count += 1  # Add this incorrect guess to the guess counter.
        elif guess > number:  # Check whether the guess is larger than the secret number.
            print("Too high.")  # Tell the player to guess a lower number.
            count += 1  # Add this incorrect guess to the guess counter.
        elif guess == number:  # Check whether the player guessed the secret number.
            count += 1  # Include the correct guess in the total number of tries.
            print(f"You guessed it in {count} tries.\n")  # Display the number of tries followed by a blank line.
            return  # End this round and return to the caller.

def main():  # Define the main function that manages the game and replay option.
    display_title()  # Call the function that displays the game title.
    
    again = "y"  # Set the initial response so the game runs at least once.
    while again.lower() == "y":  # Continue playing while the response is y, ignoring capitalization.
        limit = get_limit()  # Ask for the upper limit and store the returned value.
        play_game(limit)  # Play one round with the chosen upper limit.
        
        again = input("Play again? (y/n): ")  # Ask whether the player wants another round.
        print()  # Print a blank line for spacing.
    print("Bye!")  # Display a farewell message when the player stops playing.

# if started as the main module, call the main function
if __name__ == "__main__":  # Check whether this file is being run directly.
    main()  # Call the main function to start the game.

