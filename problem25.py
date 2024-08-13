#  Make a program that reads three numbers, and displays them on the
# screen in ascending order.

import numpy as np
numbers = []

for i in range(1,4):
    num = int(input("enter the number"))
    numbers.append(num)
x = np.sort(numbers)
print(type(x))
print(x)


