# Write a program that calculates the work done by a force
# acting on an object, using the formula T = F * d, where T is the
# work, F is the applied force, and d is the distance traveled by
# the object

force = float(input("Enter the applied force on object :"))
distance = float(input("Enter the distance of object :"))

work_done = force * distance

print("The work done is :",work_done)