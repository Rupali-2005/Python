# Prints a simple pattern of stars in increasing order

rows = int(input("Enter number of rows: "))

print("Printing star pattern:")

for i in range(1, rows + 1):
    # Print i stars for row i
    print('*' * i)
