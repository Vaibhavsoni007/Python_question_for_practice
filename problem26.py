#  Make a program that reads the age of three people and how many of them
# are of legal age (age 18 or older)

age1 = int(input("enter the age of person 1 ;"))
age2 = int(input("enter the age of person 2 ;"))
age3 = int(input("enter the age of person 3 ;"))

if(age1>= 18 and age2>=18 and age3>=18):
    print("all are legal")
else:
    print("no one is lega")