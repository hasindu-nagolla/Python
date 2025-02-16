# Slicing in Python
# ========================================================
# Slicing in Python list is a way to get a subset of 
# elements from a list. It is denoted by [start:end].
# ========================================================

# ========================================================
# Section 1: List Slicing
# ========================================================
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the elements from index 2 to 4. This is called slicing.
list2 = list1[2:5]
print(list2)  # Output: [3, 4, 5]

# ========================================================
# Section 2: Slicing with [-1] and [:-1]
# ========================================================
# We can use [:-1] to get all elements without the last element.
# [-1] to get the last element.
print(list1[:-1])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[-1])   # Output: 10

# ========================================================
# Section 3: Slicing Other Data Structures
# ========================================================

# We can always slice strings, tuples, and sets in the same way as lists,
# but we cannot slice dictionaries because dictionaries are unordered.




# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
