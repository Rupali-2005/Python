# Prints Pascal's Triangle up to n rows

def factorial(num):
    """Calculates factorial of a number"""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

rows = int(input("Enter number of rows for Pascal's Triangle: "))

print("Pascal's Triangle:")

for i in range(rows):
    # Print spaces for formatting
    print(' ' * (rows - i), end='')

    # Calculate and print binomial coefficients
    for j in range(i + 1):
        val = factorial(i) // (factorial(j) * factorial(i - j))
        print(val, end=' ')
    print()  # Newline after each row
