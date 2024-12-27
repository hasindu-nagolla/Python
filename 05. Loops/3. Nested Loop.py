# ========================================================
# Section 1: Nested Loop
# ========================================================

# Nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop"

# Nested loop syntax

# for outerLoopVariable in outerLoop:
#     for innerLoopVariable in innerLoop:
#         # do something with inner loop
#     # do something with outer loop

# Example

# calculate the multiplication table of 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()  # print a new line after each iteration of the outer loop


# In loop nesting in Python, we can put any type of loop inside another loop. For example, a for loop can be inside a while loop.

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
