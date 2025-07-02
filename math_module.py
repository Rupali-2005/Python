# Demonstrates usage of math module functions

import math

num = float(input("Enter a number: "))

# Square root
print("Square root:", math.sqrt(num))

# Ceiling value
print("Ceiling value:", math.ceil(num))

# Floor value
print("Floor value:", math.floor(num))

# Power function (num^3)
print(f"{num} raised to power 3:", math.pow(num, 3))
