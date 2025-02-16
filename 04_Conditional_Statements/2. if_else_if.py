# ========================================================
# Section 1: Conditional Statement with Ranges
# ========================================================
"""
This section evaluates the marks and assigns a grade based on a given range.
- 0 - 30: Fail
- 30 - 50: S
- 50 - 60: C
- 60 - 75: B
- 75 - 100: A
"""

marks = 82

# Check the grade based on the marks range
if marks >= 0 and marks < 30:
    print("Fail")
elif marks >= 30 and marks < 50:
    print("S")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 60 and marks < 75:
    print("B")
elif marks >= 75 and marks <= 100:
    print("A")
else:
    print("Invalid Marks")

# ========================================================
# Section 2: Optimized Conditional Check
# ========================================================
"""
In this approach, we first check for invalid marks before checking the grade ranges.
This avoids unnecessary checks when marks are outside the valid range.
"""

# First check if marks are valid
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 0 and marks < 30:
    print("Fail")
elif marks < 50:
    print("S")
elif marks < 60:
    print("C")
elif marks < 75:
    print("B")
else:
    print("A")
    
    

# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================

