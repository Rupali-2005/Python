# Prints a hollow square pattern using stars

size = int(input("Enter the size of the square: "))

for i in range(size):
    for j in range(size):
        # Print star at boundary positions, else space
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print() 
