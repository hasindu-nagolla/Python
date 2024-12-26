# ========================================================
# Section 1: For Loop with List
# ========================================================

# For Loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
# Or else, we can call it a foreach loop.

x = [1, 2, 3, 4, 5]  # List

# We use the index to get the value of the list and print the value through an index of the list.
index = 0
for item in x:
    y = x[index]
    print(y)
    index += 1

# We can also use this method to get the value of the list.

# ========================================================
# Section 2: Using enumerate() to Get Index and Value
# ========================================================

# enumerate() function is used to get the index and value of the list.
for index, item in enumerate(x):
    print(index, item)

# ========================================================
# Section 3: Using range() for a Specific Number of Iterations
# ========================================================

# If we need to run a loop for a specific number of times, then we can use the range() function.
for item in range(0, 10):
    print(type)

# ========================================================
# Section 4: Iterating a Dictionary
# ========================================================

myDictionary = {
    "Age": 25,
    "Name": "Hasindu",
    "Country": "Sri Lanka",
    "City": "Colombo"
}

for key, value in myDictionary.items():
    # items() function is used to get the key and value of the dictionary.
    print(key, value)


# ========================================================
# Section 5: Iterating a Set
# ========================================================

mySet = {
    1,
    "Hasindu",
    3,
    "Lakshan",
    5
}

for item in mySet:
    # set is an unordered collection of items, so the output may not be in the order of the input.
    print(item)


# ========================================================
# Section 6: Iterating a Tuple
# ========================================================

myTuple = ("Hasindu", 2, 3, "BSE", 5)

for item in myTuple:
    # tuple is an ordered collection of items, so the output will be in the order of the input.
    print(item)


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
