#  Create a program that prompts the user for the radius of a
# sphere and calculates and displays its volume.

import math
radius = float(input("Enter the radius of sphere :"))

volume = (4/3)*math.pi* radius**3

print("the volume of the sphere is :",volume)