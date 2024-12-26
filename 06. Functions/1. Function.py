# Function in Python

# ============================================================================================================
# Function in Python is a block of code that only runs when it is called. It is defined using the def keyword.
# ============================================================================================================

# ========================================================
# Section 1: Simple Function
# ========================================================

def my_function():
    print("Hello from a function")
    
my_function() # Calling the function.

# ========================================================
# Section 2: Function to Calculate Grade
# ========================================================

def myFunction(marks, subject):
    print("Subject: ", subject)
    if marks < 0 or marks > 100:
        print("Marks are invalid")
    elif marks < 35:
        print("F")
    elif marks < 50:
        print("S")
    elif marks < 60:
        print("C")
    elif marks < 70:
        print("B")
    else:
        print("A")
        
    
myFunction(45, "Maths") # Calling the function with subject name.
myFunction(marks= 75, subject= "Science") # Calling the function with subject name and marks. It's called named argument. In this method, we can pass the value of arguments in any order.
# myFunction(marks= 75, "Science") # Cannot write positional argument after named argument. All named arguments should be written after positional arguments.


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
