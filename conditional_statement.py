# Conditional Statements in Python

num = int(input("Enter an integer: "))

if num > 0:
    print(f"{num} is positive.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is negative.")

# Even or Odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
