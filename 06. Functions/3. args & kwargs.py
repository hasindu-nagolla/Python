""" In Python, *args & **kwargs are used to pass a variable number of arguments to a function. """

# ========================================================
# Section 1: Using *args
# ========================================================

# *args(arguments) is used to pass a variable number of non-keyword arguments to a function. 
# It allows you to pass any number of positional arguments.
# If we don't know how many arguments will be passed to a function, we can use *args.

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4, 5)

# ========================================================
# Section 2: Using **kwargs
# ========================================================

# **kwargs is used to pass a variable number of keyword arguments to a function. 
# It allows you to pass any number of named arguments, which are then packed into a dictionary.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_function(name="Hasindu", age=22, city="Kandy")

# ========================================================
# Section 3: Combining *args and **kwargs
# ========================================================

# Packed arguments/positional arguments should be written first.
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, 4, 5, name="Hasindu", age=22)

# You can use both *args and **kwargs in the same function to handle both positional and keyword arguments.

# ========================================================
# Section 4: Practice - Sum of Values
# ========================================================
# Practice - 5 values and pass them to the function and print the sum of all values in the list.

def sum(*list):  # *list is used to pass multiple values to the function.
    total = 0
    for i in list:
        total += i
    print(total)  # print the sum of all values in the list.

sum(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)



# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================