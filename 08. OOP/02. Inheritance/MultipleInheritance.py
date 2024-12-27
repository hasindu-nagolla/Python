# Python Multiple Inheritance Tutorial

# ========================================================
# Section 1: Parent Classes
# ========================================================

class Animal:
    def __init__(self, breed):
        print("Animal Constructor: ")
        self.breed = breed

    def talk(self):
        print("Animal Talking")

    def move(self):
        print("Animal Moving")


class Mamel:
    def __init__(self):
        print("Mamel Constructor: ")

    def feed(self):
        print("Feeding Milk")


# ========================================================
# Section 2: Child Class with Multiple Inheritance
# ========================================================

class Dog(Animal, Mamel):  # Inheriting from both Animal and Mamel classes

    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")  # Calls the Animal constructor
        self.name = name

    def set_name(self, name):
        self.name = name

    def talk(self):  # Method overriding
        super(Dog, self).talk()  # Calls the parent class `talk` method
        print("Dog is Barking")

    def bark(self, message):
        msg = f"Woof Woof, My name is {self.name}, {message}"
        print(msg)

    # we also can override feed method in here


# ========================================================
# Section 3: Demonstration
# ========================================================

dog1 = Dog("Scooby")
dog1.feed()  # Calling the `feed` method from the Mamel class

# ========================================================
# Explanation
# ========================================================
# Multiple inheritance allows a class to inherit from more than one parent class.
# In this example, the Dog class inherits from both Animal and Mamel classes.

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
