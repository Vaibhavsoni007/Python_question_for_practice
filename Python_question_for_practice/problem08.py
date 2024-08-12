# Write a program that calculates the delta of a quadratic
# equation (Δ = b² - 4ac).

print("""suppose your equeation is of the form ax^2 + bx + c  then
        write the values of a , b and c""")
a= int(input("the value of a :"))
b= int(input("the value of a :"))
c= int(input("the value of a :"))
delta = (b*b)-4*a*c
print("the delta of quadratic equation is :",delta)
