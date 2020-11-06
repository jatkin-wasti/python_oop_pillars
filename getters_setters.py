# getters and setters
# why? - Use cases:
# Some information should be visible but some should be hidden - Seperation of concern

# Syntax is

# Step 1
# We'll create a class called Student
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

        def getstudent(self, value):
            self.__name  # __ is called dunder, its used to hide the data

        def setstudent(self, value):
            self.__name = value


student = Student("Jamie", "Sparta Global")
print("Student name is " + student.getstudent())

# Step 2, second iteration
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

        @property  # A decorator in python is any callable python object that is used to modify a function
        # function or a class
        def Student(self, value):
            print("This is a getter method. Calling @student.student method")
            self.__name  # __ is called dunder, its used to hide the data

        @Student.setter
        def Student(self, value):
            print("This is a setter method")
            self.__name = value


student = Student("Jamie", "Sparta Global")
print("Student name is " + student.name)
print("Student works in " + student.company)
