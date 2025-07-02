# Basic Date and Time operations

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

print("Formatted date:", now.strftime("%d-%m-%Y"))
print("Formatted time:", now.strftime("%H:%M:%S"))

# Parse date from string
date_str = input("Enter a date (YYYY-MM-DD): ")
try:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print("Parsed date:", date_obj)
except ValueError:
    print("Invalid date format.")
