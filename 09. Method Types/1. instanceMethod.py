# Instance Method

# ========================================================
# Section 1: Defining the Class with an Instance Method
# ========================================================

class Person:

    def __init__(self, name):
        print("Person class constructor")
        self.name = name

    # Instance method
    def print_name(self):
        print("Name: ", self.name)


# ========================================================
# Section 2: Using the Class and Calling the Instance Method
# ========================================================

user = Person("John")  # Create an instance of the class Person and assign it to the variable user
user.print_name()  # Call the instance method using the object

# In an instance method, we need to call this method. We need to create an object of the class and call the method using the object.
# Calling via instance, because it is an instance method.

# ========================================================
# Explanation
# ========================================================

# Instance methods are called on objects (instances) of the class. You cannot call these methods without creating an instance.




# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
