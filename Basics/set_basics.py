# Basic Set Operations in Python

# Create a set from space-separated input
st = {int(x) for x in input("Enter Set (space-separated integers): ").split()}

# Add an element
i = int(input("Enter element to add: "))
st.add(i)
print("After adding element:")
print("Set (sorted):", *sorted(st))

# Remove an element
r = int(input("Enter element to remove: "))
st.discard(r)  # Does not raise error if element not present
print("After removing element:")
print("Set (sorted):", *sorted(st))

# Sum of elements in the set
print("Sum of elements in the set:", sum(st))

# Check if one set is a subset of another
a = set(map(int, input("Enter Set A (space-separated): ").split()))
b = set(map(int, input("Enter Set B (space-separated): ").split()))
print("Is A a subset of B?:", a.issubset(b))

# Union of A and B
print("Union of A and B:", a | b)
