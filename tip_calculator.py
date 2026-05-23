'''
Landon Pack
IS - 303 - A04

Tip calculator

This program will calculate a bill total based on the calculated tip amound and based off of an inputted bill total 
and split it evenly amongst a specified number of people.

Inputs:
-Bill total
-Percentage to tip
-Amount of people to split the total amongst

Processes:
-get_valid_bill()Input validation to ensure that the bill total is a valid number
-get_valid_tip() Input validation of the tip percentage to ensure that it is a valid integer
-get_valid_count()Input validation on the amount of people to ensure that it is a valid integer
-calculate_tip()Tip amount calculation (Pre tip bill total * tip percentage/100 )
-calculate_bill()Bill total calculation (Pre tip bill total + tip amount)
-calculate_split() Calculates the amount that each person will owe (bill total/ amt of people)
generate_report() Generates a report outlining the information


Outputs:
-A report detailing the bill total, the amount of people to split the tip the tip percentage, tip amount and amount per person



'''

import math

def get_valid_bill():
    while True:
        try:
            original_bill = float(input("What is the original bill amount?: "))
            return original_bill
        except ValueError:
            print("Error: Unexpected value. Please enter a valid number.")

def get_valid_tip():
    while True:
        try:
            tip_percentage = int(input("What percent would you like to tip?: "))
            return tip_percentage
        except ValueError:
            print("Error: Unexpected value entered. Please enter a valid number.")

def get_valid_count():
    while True:
        try:
            guests = int(input("Amongst how many people would you like to split the bill?: "))
            return guests
        except ValueError:
            print("Error: Unexpected value. Please enter a whole number.")

def calculate_tip(bill, tip_percentage):
    return bill * (tip_percentage / 100)

def calculate_bill(bill, tip_amt):
    return bill + tip_amt

def calculate_split(final_bill, guest_count):
    return math.ceil((final_bill / guest_count) * 100) / 100

def generate_report(bill, tip_percentage, tip_amt, final_bill, guest_count, split_amt):
    print("--- Bill Splitter ---")
    print(f"Original bill:   ${bill:.2f}")
    print(f"Tip percentage:  {tip_percentage}%")
    print(f"Tip amount:      ${tip_amt:.2f}")
    print(f"Total bill:      ${final_bill:.2f}")
    print(f"Number of guests: {guest_count}")
    print(f"Amount per person: ${split_amt:.2f}")
    print("Thank you for using the Bill Splitter program!")

bill = get_valid_bill()
tip_percentage = get_valid_tip()
guest_count = get_valid_count()
tip_amt = calculate_tip(bill, tip_percentage)
final_bill = calculate_bill(bill, tip_amt)
split_amt = calculate_split(final_bill, guest_count)


generate_report(bill, tip_percentage, tip_amt, final_bill, guest_count, split_amt)
   

