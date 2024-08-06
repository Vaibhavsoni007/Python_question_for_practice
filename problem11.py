# . Write a program that calculates the average velocity of an
# object, using the formula v = Δs/Δt, where v is the average
# velocity, Δs is the space variation, and Δt is the time variation

space_variation = float(input("Enter the space variation :"))
time_variation = float(input("Enter the time variation :"))

average_velocity = space_variation/time_variation

print("average velocity is :",average_velocity)