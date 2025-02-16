# In append mode, the contents are added to the end of the file.

# ========================================================
# Section 1: Append Mode in Files
# ========================================================

with open("test.txt", "a") as myFile:
    myFile.write(
        "Opening files: Use open() with the appropriate mode ('r', 'w', 'a', etc.)." + "\n")
    myFile.write(
        "Reading files: Use read(), readline(), or readlines() methods." + "\n")
    myFile.write(
        "Writing files: Use write() or writelines() methods." + "\n")
    myFile.write(
        "Closing files: Always close files after use, preferably with a with statement." + "\n")

# ========================================================
# Explanation: 
# In this method, the file is automatically closed after the block of code is executed. 
# This is called a context manager, and it ensures that the file is properly closed without the need for explicit closing.
# ========================================================


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
