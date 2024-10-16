# Write a program that asks the user for a number N and
# says whether it is prime or not.
number = int(input("Enter the number :"))

if number < 2:
    is_prime = False
else:
    is_prime = True

    for i in range(2,int(number ** 0.5) + 1):
        if number%i == 0:
            is_prime = False
            break

if is_prime:
    print(" is prime number")
else:
    print(" is not a prime number")

