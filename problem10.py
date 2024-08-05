#  Write a program that calculates the perimeter and area of a
# triangle, using the formulas P = a + b + c and A = (b * h) / 2,
# where a, b and c are the sides of the triangle and h is the height
# relative to the side B.

a = int(input("enter the lenght of side a :"))
b = int(input("enter the lenght of side b :"))
c = int(input("enter the lenght of side c :"))
h = int(input("enter the lenght of side height :"))

perimeter = a + b + c
area = (b*h)/2

print("the perimeter of the triangle is :",perimeter)
print("the area of the triangle is :",area)