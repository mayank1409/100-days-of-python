# Day 02 - Challenge 2
# Write a Program to calculate the BMI of a person

weight_kgs_str = input("Enter the weight of person: ")
height_m_str = input("Enter the height of person: ")

weight_kgs = int(weight_kgs_str)
height_m = float(height_m_str)

bmi = weight_kgs  / (height_m ** 2)
print("Body Mass Index of person: " + str(bmi))
