# ========================================================
# Section 1: Try-Except Block to Handle Exceptions
# ========================================================
from os import path

fileName = './Error Handling/Python Error Handling Guide2.txt'

x = 10
y = 1

try:
    z = x / y
    print(z)

    with open(fileName) as file:
        print(file.readline())

except ZeroDivisionError:  # Raised when the second number is zero.
    print("Input error")
except FileNotFoundError:  # Raised when the file is not found.
    print("File not found")
except Exception:  # Base class for all exceptions.
    print("Unknown error")

# ========================================================
# Section 2: Other Common Exceptions
# ========================================================

# 1. ImportError: Raised when an import statement fails.
# 2. IndexError: Raised when a sequence subscript is out of range.
# 3. KeyError: Raised when a dictionary key is not found.
# 4. MemoryError: Raised when an operation runs out of memory.
# 5. NameError: Raised when a variable is not found in local or global scope.
# 6. NotImplementedError: Raised by abstract methods.
# 7. OSError: Raised when a system operation causes a system-related error.
# 8. SyntaxError: Raised when there is an error in Python syntax.
# 9. IndentationError: Raised when indentation is not specified properly.
# 10. TabError: Raised when indentation consists of inconsistent tabs and spaces.
# 11. TypeError: Raised when a function is called on a value of an inappropriate type.
# 12. ValueError: Raised when a function is called on a value of the correct type, but with an inappropriate value.
# 13. ZeroDivisionError: Raised when the second operand of a division or module operation is zero.
# 14. FileExistsError: Raised when trying to create a file or directory that already exists.
# 15. FileNotFoundError: Raised when a file or directory is requested but can't be found.
# 16. InterruptedError: Raised when a system call is interrupted by an incoming signal.
# 17. IsADirectoryError: Raised when a file operation is requested on a directory.
# 18. NotADirectoryError: Raised when a directory operation is requested on a file.
# 19. PermissionError: Raised when trying to run an operation without the adequate access rights.
# 20. ProcessLookupError: Raised when a given process doesn't exist.
# 21. TimeoutError: Raised when a system function times out.
# 22. ArithmeticError: Raised when numeric calculations fail.
# 23. FloatingPointError: Raised when a floating-point calculation fails.
# 24. OverflowError: Raised when a calculation exceeds the maximum limit for a numeric type.
# 25. SystemError: Raised when the interpreter detects an internal error.
# 26. ReferenceError: Raised when a weak reference proxy is used to access a garbage-collected referent.



# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================
