# Write a program that calculates and displays the sum of
# even numbers from 1 to 100 using a repeating loop.

sum = 0
for i in range(1,101):
    if (i%2==0):
        sum = i + sum
    
print("the sum is :",sum)