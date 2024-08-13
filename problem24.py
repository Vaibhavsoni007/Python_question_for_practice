# Create a program that reads three numbers and checks if their sum 
# positive, negative or equal to zero

num1 = float(input("enter the number 1 :"))
num2 = float(input("enter the number 2 :"))
num3 = float(input("enter the number 3 :"))

sum = num1+num2+num3

if(sum>0):
    print(f"{sum} is positive")
if(sum==0):
    print(f"{sum} is zero")
if(sum<0):
    print(f"{sum} is negative")