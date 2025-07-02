# Shows how to use lambda (anonymous) functions

# Lambda to add 10 to a number
add_ten = lambda x: x + 10

number = int(input("Enter a number: "))
result = add_ten(number)
print(f"Number after adding 10 using lambda: {result}")

# Lambda to multiply two numbers
multiply = lambda x, y: x * y
a = int(input("Enter first number for multiplication: "))
b = int(input("Enter second number for multiplication: "))
print(f"Multiplication result using lambda: {multiply(a, b)}")
