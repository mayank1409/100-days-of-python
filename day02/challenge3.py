# Day 02 - Challenge 3
# Write a program to tell how many weeks left in your lifetime, if you are of age Years today.

age = int(input("Enter your current age: "))
years = 90 - age
weeks = years * 52

print(f'You have {weeks} left')
