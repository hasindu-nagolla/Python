# ========================================================
# Section 1: If-Else Statement
# ========================================================
"""
The If-Else statement is used to execute a block of code if a condition is true,
and another block of code if it is false.
"""

x = 10
y = 20

# Check if x is greater than or equal to 25
if x >= 25:
    print("You Are Selected")
else:
    print("You Are Not Selected")

# Output: You Are Not Selected, it depends on the value of x.

# ========================================================
# Section 2: Example with Height
# ========================================================
height = 5.7

# If height is greater than or equal to 5.5, assign "Security" job
if height >= 5.5:
    job = "Security"
else:
    job = "Labor"

print(job)

# ========================================================
# Section 3: Ternary Operator (One-line If-Else)
# ========================================================
"""
The Ternary Operator is a shorthand for writing an if-else statement in one line.
"""

# Assign job based on height using the ternary operator
job = "Security" if height >= 5.5 else "Labor"
print(job)


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
