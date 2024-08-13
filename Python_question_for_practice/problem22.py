# Make a program that reads the grades of two tests, calculates the simple
# arithmetic mean, and informs whether the student passed (average greater
# than or equal to 6) or failed (average less than 6).

grade1 = float(input("Enter the grade of test 1 :"))
grade2 = float(input("Enter the grade of test 2 :"))

ar_mean = (grade1+grade2)/2

if(ar_mean >= 6):
    print("the student is pass")
else:
    print("the student is fail")
