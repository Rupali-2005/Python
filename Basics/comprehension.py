# List Comprehensions

nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Squares of numbers
squares = [x**2 for x in nums]
print("Squares:", squares)

# Filter even numbers
evens = [x for x in nums if x % 2 == 0]
print("Even numbers:", evens)
