# Variables are containers for storing values. Python has no command for declaring a variable.

x = 5
y = "Hello, World!"
print(x)
print(y)

# Also we dont need to declare the data type of the variable. Python will automatically assign the data type to the variable.

x = 4  # x is of type int
x = "Hello User"  # x is now of type str
print(x)

# Casting - If we want to specify the data type of a variable manually, we can use casting.

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(x, type(x)) # type() => return the data type of the variable.
print(y, type(y))
print(z, type(z))

# Case-Sensitive - Variable names are case-sensitive in Python.

y = "Hello, World!"
Y = 5 # Y and y are two different variables. not overwrite.

# Many Values to Multiple Variables - Python allows to assign values to multiple variables in one code line.

x, y, z = "User01", "User02", "User03"
print(x)
print(y)
print(z)

# One Value to Multiple Variables - Python allows to assign the same value to multiple variables in one code line.

xy = yz = zx = "User abc"
print(xy)
print(yz)
print(zx)

# Unpack a Collection - Python allows to unpack a collection of values into variables.

Countries = ["USA", "Sri Lanka", "India"]
country1, country2, country3 = Countries
print(country1, country2, country3) # print USA, Sri Lanka, India accordingly.

# Output Multiple Variables

print(country1, country2, country3)  # print USA, Sri Lanka, India accordingly.
print(country1 +  country2 + country3)  # print USA Sri Lanka India accordingly.

# Global Variables - Variables that are created outside of a function are known as global variables.

myCountry = "Sri Lanka"

def myFunc():
    print("I am from " + myCountry)

myFunc()    

# Local Variables - Variables that are created inside a function are known as local variables. cannot be accessed outside the function.

def myFunc2():
    myCity = "Kandy"
    print("I am from " + myCity)

myFunc2()