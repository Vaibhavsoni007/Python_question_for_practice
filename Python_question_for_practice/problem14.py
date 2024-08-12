# Write a program that reads the x and y position of two
# points in the Cartesian plane, and calculates the distance
# between them.

import math

# enter the coorndinate of point 1
x1 = int(input("enter the x-coordinate of point 1 :"))
y1 = int(input("enter the y-coordinate of point 1 :"))

# enter the coorndinate of point 2
x2 = int(input("enter the x-coordinate of point 2 :"))
y2 = int(input("enter the y-coordinate of point 2 :"))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 )

print("the distance between these two points is :",distance)



