# functions_basics.py

def greet(name):
    """
    This function takes a name string and prints a greeting message.
    """
    print(f"Hello, {name}! Welcome to functions basics.")

# Take name input from user
user_name = input("Enter your name: ")

# Call the function with user input
greet(user_name)
