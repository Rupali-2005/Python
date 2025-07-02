# Demonstrates basic list operations: creation, adding, removing, and looping

# Step 1: Create an empty list
fruits = []

# Step 2: Add items to the list
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")

print("List after adding fruits:", fruits)

# Step 3: Remove an item
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Step 4: Loop through the list and print each fruit
print("Printing all fruits:")
for fruit in fruits:
    print(fruit)
