# Class Method

# ========================================================
# Section 1: Defining the Class with Class Method
# ========================================================

class Person:
    
    types = ['Person', 'Animal', 'Bird']  # Class attribute
    foods = ['Rice', 'Bread', 'Fish']  # Class attribute
    
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # Instance method    
    def getName(self):
        print(self)
        print("Name: ", self.name)
  
    # Class method
    @classmethod
    def getTypes(cls):  # cls is a reference to the class itself
        print(cls)
        
    # The first argument to a class method is cls, which refers to the class (Person in this case), not an individual object.


# ========================================================
# Section 2: Using the Class and Calling the Class Method
# ========================================================

user1 = Person("John")
print(user1.getName)  # Prints the method's memory reference, not the result of calling it


print(Person.getTypes)  # Prints the memory reference of the class method
# These types of methods are called class methods.

# ========================================================
# Explanation
# ========================================================

# A class method is bound to the class and can be called on the class itself, without creating an object.
# The first argument of a class method is always the class itself, referred to as cls.


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
