# Break and Continue in While Loop is used to control the flow of the loop. (also known as loop control statements)

# ========================================================
# Section 1: Break Statement
# ========================================================

# Break statement - is used to exit the loop before the loop ends.

marks = 0
while True:  # This loop will run until we break it.

    if marks == 10:
        break  # This will break the loop when the count is equal to 10.

    print("Marks is: ", marks)
    marks += 1

# ========================================================
# Section 2: Break in For Loop
# ========================================================

# Also we can use break to for loop as well.

createList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in createList:
    if item >= 6:
        break

    print("Item is: ", item)

# ========================================================
# Section 3: Continue Statement
# ========================================================

# Continue statement - is used to skip the current iteration of the loop and continue with the next iteration.

x = [14, 25, 73, 12, 18]
count = 0

# in for loop

print("Continue statement in for loop.")
for i in x:
    if i % 2 == 0:
        continue

    print("Item is: ", i)


# ========================================================
# Section 4: Continue in While Loop
# ========================================================

print("Continue statement in while loop.")

while count < len(x) - 1:
    print("Index is: ", count)

    i = x[count]

    if i % 2 == 0:
        count += 1
        continue

    print("Item is: ", i)
    count += 1


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
