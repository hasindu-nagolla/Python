# Python Inheritance and Method Overriding Tutorial

# ========================================================
# Section 1: Parent Class
# ========================================================

class Animal:
    def __init__(self, breed):
        print("Animal Constructor: ")
        self.breed = breed

    def talk(self):
        print("Animal Talking")

    def move(self):
        print("Animal Moving")


# ========================================================
# Section 2: Child Class with Overriding
# ========================================================

class Dog(Animal):  # Inheriting from Animal class

    # Constructor overriding - stop the execution of the parent class constructor when calling the child class constructor
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")  # Explicitly calling the parent class constructor
        self.name = name

    def set_name(self, name):
        self.name = name

    # Method Overriding - redefine the method of the parent class in the child class
    def talk(self):
        # Explicitly calling the parent class method (not called by default)
        super(Dog, self).talk()
        print("Dog is Barking")

    def bark(self, message):
        msg = f"Woof Woof, My name is {self.name}, {message}"
        print(msg)


# ========================================================
# Section 3: Demonstration
# ========================================================

dog1 = Dog("Scooby")
dog1.talk()  # Demonstrating method overriding
print(dog1.breed)  # Accessing the 'breed' attribute from the parent class

# ========================================================
# Explanation
# ========================================================
# Overriding is a feature that allows us to redefine methods of the parent class in the child class.

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
