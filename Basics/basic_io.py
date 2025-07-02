# Basic I/O in Python

# Input and print a string
s = input("Enter a string: ")
print("You entered:", s)

# Take integer input and add 10, then print
n = int(input("Enter an integer: "))
print("Integer + 10 =", n + 10)

# Take floating-point input and multiply by 10, then print
f = float(input("Enter a float: "))
print("Float * 10 =", f * 10)

# Inputs for string operations
a = input("Enter value for a: ")
b = input("Enter value for b: ")
separator = input("Enter a separator character: ")[0]

# Different ways to print a and b
print(a, b)                  # With space and newline
print(a, b, end='')          # With space, no newline
print("\n" + a + separator + b)  # With separator and newline
print(a + b)                 # Concatenated directly

# Multi Printing
n = int(input("\nEnter how many times to repeat a: "))
print(a * n)

# Complex repetition with separator
c = input("Enter separator c: ")

# Ensure a and b are digits to safely cast
if a.isdigit() and b.isdigit():
    print(a * int(a) + c + b * int(b))
else:
    print("Error: a and b must be digits for repetition.")
