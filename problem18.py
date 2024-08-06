# Write a program that asks the user for three numbers and displays the
# largest one.

num1 = float(input("Enter the 1st number :"))
num2 = float(input("Enter the 2nd number :"))
num3 = float(input("Enter the 3rd number :"))

if(num1>=num2 and num1>=num3):
    print(f"{num1} is bigger than {num2} and {num3}")
elif(num2>=num1 and num2>=num3):
    print(f"{num2} is bigger than {num1} and {num3}")
elif(num3>=num2 and num3>=num1):
    print(f"{num3} is bigger than {num2} and {num1}")




