#  Write a program that calculates the perimeter and area of a
# rectangle, using the formulas P = 2(w + l) and A = wl, where w
# is the width and l is the length

length = float(input("enter the length of rectangle "))
width = float(input("enter the width of rectangle "))

perimeter = 2*(width+length)
area = length*width

print("perimeter of the rectangle is :",perimeter)
print("area of the rectangle is :",area)