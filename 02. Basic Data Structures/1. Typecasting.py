# Type Conversion (Typecasting) in Python
# ========================================================
# Type conversion is the process of converting one data type into another data type.
# ========================================================

# Converting int to float
num_int = 10
num_float = float(num_int)  # float() function converts int to float
print("Integer:", num_int)
print("Float:", num_float)

# ========================================================

# Converting float to int
num_float = 10.5
num_int = int(num_float)  # int() function converts float to int
print("Float:", num_float)
print("Integer:", num_int)

# ========================================================

# Converting int to string
num_int = 10
num_str = str(num_int)  # str() function converts int to string
print("Integer:", num_int)
print("String:", num_str)

# ========================================================

# Converting string to int
num_str = "10"
num_int = int(num_str)  # int() function converts string to int
print("String:", num_str)
print("Integer:", num_int)

# ========================================================

# Converting float to string
num_float = 10.5
num_str = str(num_float)  # str() function converts float to string
print("Float:", num_float)
print("String:", num_str, type(num_str))

# ========================================================

# Converting string to float
num_str = "10.5"
num_float = float(num_str)  # float() function converts string to float
print("String:", num_str)
print("Float:", num_float, type(num_float))

# ========================================================

# Converting string to list
num_str = "10, 20, 30, 40, 50"
num_list = num_str.split(", ")  # split() function converts string to list
print("String:", num_str)
print("List:", num_list, type(num_list))

# ========================================================

# Converting list to string
num_list = ["10", "20", "30", "40", "50"]
num_str = ", ".join(num_list)  # join() function converts list to string
print("List:", num_list)
print("String:", num_str, type(num_str))


# Note: We can perform conversions with other data types as well, including data structures like tuple, set, dictionary, etc.

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
