# Butterfly Pattern Program
n = int(input("Enter number of rows: "))

# The butterfly pattern has two halves: upper and lower

# Upper half of the butterfly
for i in range(1, n + 1):
    # Print left wing stars (i stars)
    left_wing = '*' * i

    # Print spaces between wings
    spaces = ' ' * (2 * (n - i))

    # Print right wing stars (i stars)
    right_wing = '*' * i

    # Combine left wing + spaces + right wing
    line = left_wing + spaces + right_wing

    print(line) 

# Lower half of the butterfly
for i in range(n, 0, -1):
    # Print left wing stars (i stars)
    left_wing = '*' * i

    # Print spaces between wings
    spaces = ' ' * (2 * (n - i))

    # Print right wing stars (i stars)
    right_wing = '*' * i

    # Combine left wing + spaces + right wing
    line = left_wing + spaces + right_wing

    print(line)  # Print the current line
