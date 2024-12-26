""" 
Reading a file using the read() method
"""

# ========================================================
# Section 1: Read entire file using read()
# ========================================================

myFile = open("./File input output/dataFile.txt")
print(myFile.read())  # Read the entire file

# ========================================================
# Section 2: Read file using readline()
# ========================================================

print(myFile.readline())  # Read the first line

# ========================================================
# Section 3: Read file line by line using while loop
# ========================================================

while True:
    contents = myFile.readline()
    if not contents:
        break
    print(contents, end="")

# ========================================================
# Section 4: Read file line by line using for loop
# ========================================================

for line in myFile:
    print("Line --> ", line)

# ========================================================
# Close the file after reading
# ========================================================

myFile.close()


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
