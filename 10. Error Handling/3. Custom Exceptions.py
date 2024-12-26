# ========================================================
# Section 1: Custom Exception Classes
# ========================================================

class InvalidAgeError(Exception):
    """Custom exception raised when the age is invalid."""
    def __init__(self, error):
        super(InvalidAgeError, self).__init__(error)

class InvalidNameError(Exception):
    """Custom exception raised when the name is invalid."""
    def __init__(self, error):
        super(InvalidNameError, self).__init__(error)

# ========================================================
# Section 2: Person Class Definition
# ========================================================

class Person:
    """Class to represent a Person with a name and age."""
    
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
    
    @staticmethod
    def get_person(name, age):
        """
        Factory method to create a Person object.
        Raises InvalidNameError if the name is empty.
        Raises InvalidAgeError if the age is not within valid range.
        """
        if not name:
            raise InvalidNameError("Name is required")
        if age < 0 or age > 120:
            raise InvalidAgeError("Age is invalid")
        
        return Person(name, age)

# ========================================================
# Section 3: Exception Handling
# ========================================================

try:
    # Attempt to create a Person object with invalid input.
    person = Person.get_person("", -31)
    print(person)
except Exception as e:
    # Catch and print the error message.
    print("Error: ", e)


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
