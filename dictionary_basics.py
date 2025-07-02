# Step 1: Create a dictionary with keys and values
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Step 2: Print entire dictionary
print("Student dictionary:", student)

# Step 3: Access values by key
print("Student's name:", student["name"])
print("Student's age:", student["age"])

# Step 4: Add a new key-value pair
student["university"] = "XYZ University"
print("Updated dictionary:", student)

# Step 5: Loop through dictionary keys and values
print("All student info:")
for key, value in student.items():
    print(f"{key}: {value}")
