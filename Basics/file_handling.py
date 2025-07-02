# file_handling.py

# Step 1: Write some text to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("We are learning file handling in Python.\n")

print("Data written to 'sample.txt'.")

# Step 2: Read the contents of the file and print them
with open("sample.txt", "r") as file:
    content = file.read()

print("Reading from 'sample.txt':")
print(content)
