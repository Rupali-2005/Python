# Basic example of a class and object in Python

class Person:
    def __init__(self, name, age):
        """
        Constructor method to initialize name and age of person.
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Method to print a greeting message.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of Person class
person1 = Person("John", 25)

# Call the greet method
person1.greet()
