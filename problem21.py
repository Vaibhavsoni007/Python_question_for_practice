#  Make a program that reads the scores of two tests and reports whether the
# student passed (score greater than or equal to 6) or failed (score less than 6)
# in each of the tests.

score1 = float(input("Enter the score of test 1 :"))
score2 = float(input("Enter the score of test 2 :"))

if(score1 >= 6 and score2 >= 6):
    print("student is pass")
else:
    print("student fails")
