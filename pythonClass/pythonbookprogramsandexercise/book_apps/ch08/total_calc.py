#!/usr/bin/env python3

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid integer. Please try again.") 

def main():
    print("The Total Calculator program\n")

    # get the price and quantity
    price = get_float("Enter price: ")
    quantity = get_int("Enter quantity: ")
    
    # calculate the total
    total = price * quantity

    # display the results
    print()
    print("PRICE:    ", price)
    print("QUANTITY: ", quantity)
    print("TOTAL:    ", total)


if __name__ == "__main__":
    main()
