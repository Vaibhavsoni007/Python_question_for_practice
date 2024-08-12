# Write a program that reads two numbers and tells you which one is
# bigger.

num1 = float(input("Enter a first number"))
num2 = float(input("Enter a second number"))

if(num1>num2):
    print(f"{num1} is bigger than {num2}")
else:
    print(f"{num2} is bigger than {num1}")
