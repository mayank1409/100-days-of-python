# Day 02 - Challenge 1
# Write a Program to take a 2 digit number as input and sum the digits.

num = input("Enter a 2 digit number: ")
num_str = str(num)

if len(num_str) > 2:
    print("Invalid input")
else:
    print("Sum of digits: " + str(int(num_str[0]) + int(num_str[1])))
