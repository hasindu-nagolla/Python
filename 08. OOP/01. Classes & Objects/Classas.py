# ========================================================
# Section 1: Introduction to OOP
# ========================================================

# OOP is a programming paradigm that uses "objects" and "classes".
# It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes),
# which are used to create individual instances of objects.

# ========================================================
# Section 2: Defining a Class and Creating Objects
# ========================================================

# Define a class
class Me:  # Class names should follow the convention of being capitalized.
    pass  # `pass` is a keyword that does nothing. It is used when a statement is required syntactically but you do not want any command or code to execute.

# Create an object of the class
me1 = Me()  # `me1` is an object of the class `Me`

# Assign attributes to the object
me1.name = "name"
me1.age = 25

print(me1.name, me1.age)

# ========================================================
# Section 3: Defining a Class with Methods
# ========================================================

class Person:
    # Method to set the name attribute
    def set_name(self, name):
        self.name = name

    # Method for running action
    def Run(self):
        print("I am running")

    # Method for walking action
    def Walk(self):
        print("I am walking")

# Create an object of the class Person
person1 = Person()
person1.set_name("pass name here")
print(person1.name)



# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
