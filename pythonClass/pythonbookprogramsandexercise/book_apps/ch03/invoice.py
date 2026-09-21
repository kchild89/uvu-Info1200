#!/usr/bin/env python3

# display a welcome message
print("The Invoice program")
print()

# get user entries
customer_type = input("Enter customer type (r/w):\t")
invoice_total = float(input("Enter invoice total:\t\t"))
print()

# determine discount based on customer type and invoice total
match customer_type.lower():
    case "r":                     # retail customers
        if 0 < invoice_total < 100:
            discount_percent = 0
        elif 100 <= invoice_total < 250:
            discount_percent = .1
        elif 250 <= invoice_total < 500:
            discount_percent = .2
        elif 500 <= invoice_total:
            discount_percent = .25
    case "w":                     # wholesale customers
        if 0 < invoice_total < 500:
            discount_percent = .4
        elif 500 <= invoice_total:
            discount_percent = .5
    case _:                       # neither retail or wholesale
        discount_percent = 0
    
# calculate discount amount and new invoice total
discount_amount = round(invoice_total * discount_percent, 2)
new_invoice_total = invoice_total - discount_amount                                         
                    
# display the results
print(f"Invoice total:\t\t{invoice_total}")
print(f"Discount percent:\t{discount_percent}")
print(f"Discount amount:\t{discount_amount}")
print(f"New invoice total:\t{new_invoice_total}")                      
print() 
print("Bye!")


