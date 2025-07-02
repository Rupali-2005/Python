# Demonstrates simple regular expression matching

import re

text = input("Enter a text: ")
pattern = input("Enter a regex pattern to search for: ")

# Search for the pattern in the text
match = re.search(pattern, text)

if match:
    print(f"Pattern '{pattern}' found at position {match.start()} to {match.end()}.")
else:
    print(f"Pattern '{pattern}' not found in the text.")
