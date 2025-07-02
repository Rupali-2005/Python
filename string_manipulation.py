# Demonstrates common string operations

text = input("Enter a string: ")

# Length of string
print("Length of string:", len(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Check if string starts with 'a'
print("Starts with 'a'?", text.startswith('a'))

# Find index of first occurrence of 'a'
index = text.find('a')
if index != -1:
    print(f"First 'a' found at index {index}")
else:
    print("'a' not found in string")

# Replace spaces with hyphens
print("Replace spaces with '-':", text.replace(' ', '-'))
