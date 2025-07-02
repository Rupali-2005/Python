# Prints a diamond pattern of stars

rows = int(input("Enter number of rows for diamond (half size): "))

# Upper part of diamond (pyramid)
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Lower part of diamond (inverted pyramid)
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
