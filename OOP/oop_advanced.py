# Shows inheritance and method overriding in Python OOP

# Parent class
class Animal:
    def sound(self):
        print("Some generic animal sound")

# Child class inheriting Animal
class Dog(Animal):
    def sound(self):
        # Method overriding
        print("Bark bark!")

# Child class inheriting Animal
class Cat(Animal):
    def sound(self):
        print("Meow meow!")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call methods
print("Animal sound:")
animal.sound()

print("Dog sound:")
dog.sound()

print("Cat sound:")
cat.sound()
