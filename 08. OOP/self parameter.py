# ========================================================
# Section 1: The `self` Keyword and Constructor
# ========================================================

# The `self` keyword is a reference to the current instance of the class
# and is used to access variables and methods that belong to the class.

# ========================================================
# Section 2: Defining a Class with Constructor and Methods
# ========================================================

class Dog:
    """
    A simple class to represent a Dog.
    """

    # Constructor (__init__) is called automatically when an object is created.
    # The default value of `name` is "Unknown". If you forget to pass a name, it will be set to "Unknown".
    def __init__(self, name="Unknown"):
        self.name = name

    # Method to set the name of the dog
    def set_name(self, name):
        self.name = name

    # Method for the dog to bark
    def bark(self, message):
        msg = f"{self.name} says {message}"
        print(msg)

    # Method for the dog to walk
    def walk(self, path):
        msg = f"{self.name} is walking on {path}"
        print(msg)

# ========================================================
# Section 3: Creating Objects and Using Methods
# ========================================================

# Create an object of the class Dog (dog1)
dog1 = Dog("Tommy")  # Name is explicitly set to "Tommy"
dog1.bark("I am barking")
dog1.walk("the road")

# Create another object of the class Dog (dog2)
dog2 = Dog()  # Name is automatically set to "Unknown"
dog2.bark("I am barking")
dog2.walk("the road")

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
