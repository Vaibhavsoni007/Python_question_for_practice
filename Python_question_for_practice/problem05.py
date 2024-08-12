#  Write a program that calculates the BMI of an individual,
# using the formula BMI = weight / height²

weight = float(input("enter the weight of your body (in kg):"))
height = float(input("enter the height of your body (in m):"))

BMI = weight/height**2

print("your BMI is :",BMI)
if (BMI<=18.5):
    print("you are underweight")
if (BMI>=18.5 and BMI<=24.9):
    print("you are normal")
if (BMI>=25 and BMI<=29.9):
    print("you are overweight")
if (BMI>=30):
    print("you are obese")
