# Make a program that reads three numbers, and informs if their sum is
# divisible by 5 or not.

num1 = float(input("Enter the number 1 :"))
num2 = float(input("Enter the number 2 :"))
num3 = float(input("Enter the number 3 :"))

sum_of_3_number = num1+num2+num3

if (sum_of_3_number%5 == 0):
    print("the sum is divisible by 5 ")
else:
    print("the number is not divisible by 5")