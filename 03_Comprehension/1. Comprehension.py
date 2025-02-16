# ========================================================
# Section 1: Introduction to Comprehensions
# ========================================================
"""
Comprehension is a way to create data structures using other data structures.
Comprehensions provide a concise way to create lists, sets, and dictionaries
from existing data.
"""

# ========================================================
# Section 2: List Comprehension
# ========================================================
"""
List Comprehension - Create lists by iterating over an iterable and specifying
the expression to be included in the list.
"""

# Create a list using values of another list
listA = [1, 2, 3, 4, 5]
listB = [i for i in listA]  # Create listB using listA
print("List A:", listA, "List B:", listB)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# ========================================================
# Section 3: Set Comprehension
# ========================================================
"""
Set Comprehension - Similar to list comprehensions but creates a set instead of a list.
"""

# Create a set of squares of numbers from 0 to 9
squareSet = {x**2 for x in range(10)}
print("Set of Squares:", squareSet)

# ========================================================
# Section 4: Dictionary Comprehension
# ========================================================
"""
Dictionary Comprehension - Create dictionaries by iterating over an iterable and specifying key-value pairs.
Syntax: {key_expression: value_expression for item in iterable}
"""

# Create a dictionary with numbers as keys and their squares as values
squareDict = {x: x**2 for x in range(10)}
print("Dictionary of Squares:", squareDict)




# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
