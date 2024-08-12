# Write a program that calculates the geometric mean of three
# numbers entered by the user

import math

num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))
num3 = float(input("enter the third number :"))

product = num1*num2*num3
geometric_mean = math.pow(product,1/3)

print("geometric mean:",geometric_mean)
