# ========================================================
# Section 1: Introduction to Conditional Comprehensions
# ========================================================
"""
Conditional comprehensions allow us to include a condition that filters the
elements used in the comprehension.
Syntax: [expression for item in iterable if condition]
"""

# ========================================================
# Section 2: Conditional List Comprehension
# ========================================================
"""
Conditional List Comprehension:
Create a list by applying a condition to include only specific elements.
"""

# Create a list of squares of even numbers from 0 to 9
evenSquares = [x**2 for x in range(10) if x % 2 == 0]
print("List of Squares of Even Numbers:", evenSquares)

# ========================================================
# Section 3: Conditional Set Comprehension
# ========================================================
"""
Conditional Set Comprehension:
Create a set by applying a condition to include only specific elements.
"""

# Create a set of squares of even numbers from 0 to 9
evenSquaresSet = {x**2 for x in range(10) if x % 2 == 0}
print("Set of Squares of Even Numbers:", evenSquaresSet)

# ========================================================
# Section 4: Conditional Dictionary Comprehension
# ========================================================
"""
Conditional Dictionary Comprehension:
Create a dictionary by applying a condition to include only specific key-value pairs.
"""

# Create a dictionary with only even numbers as keys and their squares as values
evenSquareDict = {x: x**2 for x in range(10) if x % 2 == 0}
print("Dictionary of Even Numbers and Their Squares:", evenSquareDict)



# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
