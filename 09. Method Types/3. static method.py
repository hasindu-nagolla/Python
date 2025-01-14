# Static Methods in Python - Static methods are similar to class methods, but they don't receive any additional arguments; 
# they are identical to normal functions that belong to a class.

# ========================================================
# Section 1: Defining the Class with Static Method
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
    
    # Static method
    @staticmethod
    def getFoods():
        print("Foods: ", Person.foods)


# ========================================================
# Section 2: Using the Class and Calling the Static Method
# ========================================================

user1 = Person("John")
print(user1.getName)  # Prints the method's memory reference, not the result of calling it

user1.getFoods()  # Calling the static method using the object

# ========================================================
# Explanation
# ========================================================

# Static methods do not receive any reference to the instance or class. They are regular functions that belong to a class.
# You can call them on the class or object, but they do not have access to instance or class-specific data unless passed explicitly.



# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
