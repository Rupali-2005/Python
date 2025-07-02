# Demonstrates reading and writing JSON data

import json

# Sample dictionary
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Machine Learning", "Data Analysis"]
}

# Convert dictionary to JSON string
json_str = json.dumps(data, indent=4)
print("JSON string:")
print(json_str)

# Convert JSON string back to dictionary
data_parsed = json.loads(json_str)
print("Parsed dictionary:")
print(data_parsed)
