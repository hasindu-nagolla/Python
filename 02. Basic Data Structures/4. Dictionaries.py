# Python Dictionary Tutorial

# ========================================================
# Section 1: Basics of Dictionaries
# ========================================================

# Dictionaries is a collection of key-value pairs.

# Create a dictionary.
myDictioanry = {'1000': "Matale",
                '2000': "Kandy",
                '3000': "Colombo",
                '4000': "Galle",
                '4000': "Matara"}  # If we add a key-value pair with the same key, it will replace the existing value.

newDict = dict(name = "Hasindu", age = 23)  # Create a dictionary using dict() function.
print(newDict)

myDictioanry['1200'] = "Kurunegala" # Add a new key-value pair to the dictionary.

# Add a new key-value pair to the dictionary. we can add any type of key and value. this is integer key.
myDictioanry[10] = "Anuradhapura"
print(myDictioanry)

print(len(myDictioanry))  # Get the length of the dictionary.
print(type(myDictioanry))  # Get the type of the dictionary.

# Access the value of the key '1000'. we cannot use index to access the value.
y = myDictioanry['1000']
print(y)

print(myDictioanry.keys())  # Get all the keys of the dictionary.
print(myDictioanry.values())  # Get all the values of the dictionary.

# ========================================================
# Section 2: Adding Lists and Complex Data Types
# ========================================================

myDictioanry2 = {10: "Science", 20: "Maths", 30: "History", 40: "English"}

# also we can add a list as a value.
myDictioanry2[50] = ["Biology", "Chemistry"]
print(myDictioanry2)

# ========================================================
# Section 3: Accessing Values Safely
# ========================================================

myDictioanry3 = {1: 'A', 2: 'B'}

# get() method returns the value of the key. if the key is not in the dictionary, it will return None. but we can set a default value
# to return if the key is not in the dictionary.

getValue = myDictioanry3.get(1)  # Get the value of the key 1.
print(getValue)

# Get the value of the key 4. if the key is not in the dictionary, return 0.
getValue2 = myDictioanry3.get(4, 0)
print(getValue2)

# ========================================================
# Section 4: Deleting and Clearing Dictionary Elements
# ========================================================

# Delete a key-value pair from the dictionary.

myDictioanry4 = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print(myDictioanry4)

# Delete the key 1 from the dictionary. we use key to delete the key-value pair. value is automatically deleted.
del myDictioanry4[1]
print(myDictioanry4)

myDictioanry4.clear()  # Clear the dictionary.
print(myDictioanry4)

# ========================================================
# Section 5: Handling Complex Data Types
# ========================================================

#  Add complex data types as values to the dictionary.

xDic = {
    "a": ['Hello', 'Hi', 'Hey'],
    "b": ('Apple', 'Banana', 'Cherry'),
}
print(xDic)

getY = xDic['a']  # Get the value of the key 'a'.
print(getY)

getY.append('Hola')  # Add 'Hola' to the list.
print(getY)

xDic['b'] = ('Apple', 'Banana', 'Cherry', 'Mango')  # Change the value of the key 'b'.
print(xDic)

xDic.update({'b': 2024})  # Update the value of the key 'b'.
print(xDic)

# see it, you do anything to y, it will affect the dictionary. but it will not affect if "a" is a basic data type. like integer.
print(xDic)

# ========================================================
# Section 6: Nested Dictionaries
# ========================================================

# Dictionary of dictionaries.

europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}
          }

# print the capital of france.
print(europe['france']['capital'])

# create sub-dictionary data.
data = {'capital': 'colombo', 'population': 21.2}

# add data to europe dictionary.
europe['sri lanka'] = data

# print europe dictionary.
print(europe)

# ========================================================
# Section 7: Looping Through Dictionaries
# ========================================================

# Loop Dictionaries in Python.

numbersDictioanry = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

for x in numbersDictioanry:
    print(x)  # Print the keys of the dictionary.

for x in numbersDictioanry:
    print(numbersDictioanry[x])  # Print the values of the dictionary.

for x in numbersDictioanry.values():
    print(x)  # Also can use .values() to get the values of the dictionary.

for x, y in numbersDictioanry.items():
    print(x, y)  # Print the both key-value pairs of the dictionary.
