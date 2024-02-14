# Day 02 - Project 2
# Tip calculator

print("Welcome to the Tip calculator")
bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15 ? \n")) / 100
persons = int(input("How many person to split the bill? \n"))

tip = (bill * tip_percentage)
bill_with_tip = bill + tip
bill_per_person = round(bill_with_tip / persons, 2)

print(f"Total Bill is ${bill_with_tip}, Each person should pay ${bill_per_person}")
