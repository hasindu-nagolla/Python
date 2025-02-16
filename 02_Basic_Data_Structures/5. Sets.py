# Set Tutorial

# ========================================================
# Section 1: Basics of Sets
# ========================================================

# Set is a collection of unordered elements. It is mutable and has no duplicate elements.

# Create a set. 

numbers = {1, 2, 3, 4, 5}

# same to the dictionary, but don't have key-value pairs.
mySet = {"Hello", "World", "Hello"}

# see it will not have duplicate elements. The above set has two "Hello" elements, but it will only have one.
print(mySet)
print(type(mySet)) # Check type of the set.

mySet.add("Python")  # Add a new element to the set.
print(mySet)
mySet.remove("Hello")  # Remove an element from the set.
print(mySet)

# ========================================================
# Section 2: Union of Sets
# ========================================================

# add two sets together.
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

# Add two sets together. union() method will return a new set with all the elements of both sets.
addedSet = set1.union(set2)
print(addedSet)

# also we can use | (pipe) operator to add two sets together.
addedSet1 = set1 | set2
print(addedSet1)

# ========================================================
# Section 3: Subtraction of Sets
# ========================================================

# Subtract two sets.
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}

# Subtract set6 from set5. it will return a new set with the elements that are in set5 but not in set6.
SubtractedSet = set5 - set6
print(SubtractedSet)

# Get the length of the set.
print(len(SubtractedSet))

# Set items can be of any data type.
set3 = {1, 2, 3, "Hello", "World", (4, 5, 6)}
print(set3)

# ========================================================
# Section 4: Accessing Elements
# ========================================================


## We cannot access individual elements of a set. We can only access all the elements together using a loop.
exSet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in exSet:
    print(i)

## Check the specific element is in the set or not.
print(1 in exSet)

## Check the specific element is not in the set.
print(11 not in exSet) 

# ========================================================
# Section 5: Adding Items
# ========================================================

## Add elements to the set using the add() method.
createdSet = {1, 2, 3, 4, 5}
createdSet.add(6)
print(createdSet)

## Add items from another set to the current set using the update() method.
createNewSet = {6, 7, 8, 9, 10}
createdSet.update(createNewSet)
print(createdSet)

createNewSet.update([11, 12, 13, 14, 15]) # also we can add items from a list like this.
print(createNewSet)

# ========================================================
# Section 6: Removing Items
# ========================================================

## Remove an item from the set using the remove() method.
set7 = {1, 2, 3, 4, 5}
set7.remove(5)
print(set7)

## Remove an item from the set using the discard() method.
set8 = {1, 2, 3, 4, 5}
set8.discard(4)
print(set8)

## Clear the set using the clear() method.
set9 = {1, 2, 3, 4, 5}
set9.clear()
print(set9)

## Delete the set using the del keyword.
set10 = {1, 2, 3, 4, 5}
del set10
# print(set10)  # It will raise an error because the set is deleted.




# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
