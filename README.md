# OOP
### Step 1:
- Creating an Animal class as our Parent class'
```
class Animal:

    def __init__(self):  # Initialising the Animal class
        self.alive = True  # Creating an attribute/variable
        self.spine = True
        self.lungs = True
        self.eyes = True

    def breathe(self):  # Creating behaviours as methods
        return "Keep breathing to stay alive"

    def move(self):
        return "Forwards, backwards, left, and right"

    def eat(self):
        return "Consume to stay alive"

    def procreate(self):
        return "Find a mate"
```
- This contains both class attributes and class functions (methods) that all Animals
and children classes will have accress to
### Step 2:
- Creating a Reptile class as a Child class of Animal
- Why? So that we can Inherit behaviour (functions) and characteristics (variables) from the Parent class
- This uses **Abstraction**
```
from animal import Animal  # Syntax to import is from file_name import Class_name


# Creating Reptile class as a child class of the Animal class
class Reptile(Animal):
    def __init__(self):
        super().__init__()  # Super key word is used to inherit something from a parent class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    #creating functions for our Reptile class
    def seek_heat(self):
        return "You are cold blooded so stay in warm areas"

    def hunt(self):
        return "Find prey so that you can survive"

    def use_venom(self):
        return "If attacked, use this to ensure your survival"
```
### Step 3:
- Creating a Snake class as a Child class of Reptile
### Step 4:
- Creating a Python class as a Child class of Snake
## Name and main
``` __name__``` and ```__main__``` are used to check if the code is run from the current file
or from a different/imported file
- We will create 2 files and use ```__name__``` and ```__main__``` in both files to show the
the difference in outcome
## Getters and Setters
```
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company
```
- getters method with hidden information
```
        def getstudent(self, value):
            self.__name  # __ is called dunder, its used to hide the data
```
- defining a setters function
```
        def setstudent(self, value):
            self.__name = value
```
**Second Iteration**
```
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company
```
- Using @property decorator
```
@property  
        # function or a class
        def Student(self, value):
            print("This is a getter method. Calling @student.student method")
            self.__name  # __ is called dunder, its used to hide the data
```
- A decorator in python is any callable python object that is used to modify a function
- Creating the setter with a decorator
```
@Student.setter
        def Student(self, value):
            print("This is a setter method")
            self.__name = value
```
- Creating an object with required information
```
student = Student("Jamie", "Sparta Global")
print("Student name is " + student.name)
print("Student works in " + student.company)
```
