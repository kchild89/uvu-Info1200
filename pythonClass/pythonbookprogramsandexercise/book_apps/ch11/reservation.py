#!/usr/bin/env python3

from datetime import datetime, date
import locale

def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            # convert from datetime to date to make comparisons easier
            return date(dt.year, dt.month, dt.day)
        except ValueError:
            print("Invalid date format. Try again.")
            print()

def get_arrival_date():
    while True:
        arrival_date = get_date("Enter arrival date (YYYY-MM-DD): ")
        
        if arrival_date < date.today():
            print("Arrival date must be today or later. Try again.")
            print()
        else:
            return arrival_date

def get_departure_date(arrival_date):
    while True:
        departure_date = get_date("Enter departure date (YYYY-MM-DD): ")
        
        if departure_date <= arrival_date:
            print("Departure date must be after arrival date. Try again.")
            print()
        else:
            return departure_date

def main():    
    print("The Hotel Reservation program\n")

    again = "y"
    while again.lower() == "y":
        # get datetime objects from user
        arrival_date = get_arrival_date()
        departure_date = get_departure_date(arrival_date)
        print()

        # calculate nights and cost
        rate = 85.0
        rate_message = ""
        if arrival_date.month == 8:    # August is high season
            rate = 105.0
            rate_message = "(High season)"
        total_nights = (departure_date - arrival_date).days
        total_cost = rate * total_nights

        # format results
        date_format = "%B %d, %Y"
        locale.setlocale(locale.LC_ALL, "en_US")
        print(f"Arrival Date:    {arrival_date:{date_format}}")
        print(f"Departure Date:  {departure_date:{date_format}}")
        print(f"Nightly rate:    {locale.currency(rate)} {rate_message}")
        print(f"Total nights:    {total_nights}")
        print(f"Total price:     {locale.currency(total_cost)}")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")
         
if __name__ == "__main__":
    main()
