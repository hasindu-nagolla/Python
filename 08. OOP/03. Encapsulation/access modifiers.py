# Access Modifiers (Public, Private, Protected) - are used to restrict the access to some components of the class.

# ========================================================
# Section 1: Parent Class with Access Modifiers
# ========================================================

class Person:
    def __init__(self, name):
        self.name = name  # name is public attribute
        # self.age = 22 
        self.__age = 22  # Now, age is private attribute
        self._city = "Kandy"  # Now, city is protected attribute
    
    # Setter method
    def set_age(self, age):
        self.__age = age
    
    # Getter method   
    def get_age(self):
        return self.__age

    def sleep(self):
        print(self.name, "is Sleeping")


# ========================================================
# Section 2: Using the Class and Access Modifiers
# ========================================================

user = Person("John")
user.sleep()

# We also can access the age attribute directly and change it, which is not good. To prevent this, we can use encapsulation (Access Modifiers => Public, Private, Protected)

# print(user.age) 
# user.age = 25
# print(user.age)

# After adding the get_age method, we can access the age attribute indirectly
print(user.get_age())

# After adding the set_age method, we can change the age attribute indirectly
user.set_age(25)
print("After set age:", user.get_age())

## This method is called Encapsulation or Data Hiding. In this method, we can restrict the access to some components of the class.


# ========================================================
# Section 3: Child Class with Inherited Access Modifiers
# ========================================================

class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)
    
    # def print_age(self):
    #     print("Age: ", self.__age)
        
    def print_city(self):
        print("City: ", self._city)
        
user2 = Student("Alice")

# user2.print_age()  # Also, we can't access the private attribute in the child class. To access the private attribute in the child class, we can use the protected attribute.

user2.print_city()  # Also, we can access the protected attribute in the child class.

# ========================================================
# Explanation
# ========================================================
# Private = Only accessible within the class
# Protected = Accessible within the class and child classes
# Public = Accessible within the class, child classes, and outside the class


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindume/
# ========================================================
