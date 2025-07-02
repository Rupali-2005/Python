# Prints a pyramid pattern using stars

rows = int(input("Enter number of rows for pyramid: "))

print("Pyramid pattern:")
for i in range(1, rows + 1):
    # Print spaces for left padding
    print(' ' * (rows - i), end='')
    # Print stars (2*i - 1 for odd number of stars in each row)
    print('*' * (2 * i - 1))
