# Kevin Child — validation module for the Future Value app

def get_float(prompt, low, high): 
    while True:
        try:
            value = float(input(prompt))
            if low < value <= high:
                return value
            else:
                print(f"Enter a number between {low} and {high}.")   
        except ValueError:
            print("Please enter a valid number.")

def get_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low < value <= high:
                return value
            else:
                print(f"Enter an integer between {low} and {high}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    choice = "y"
    while choice.lower() == "y":
        floatValue = get_float("Enter a number greater than 0 and up to 1000:\t", 0, 1000)
        intValue = get_int("Enter an integer greater than 0 and up to 50:\t", 0, 50)
        print(floatValue)
        print(intValue)

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
        
if __name__ == "__main__":
    main()