# Creating an animal class as a SUPER/PARENT/BASE class

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


# Instantiate our class / create an object
# cat = Animal()  # Creating an object of the Animal class
# We have abstracted the move() method from our parent class
# print(cat.move())  # We can see it has inherited all functionality and characteristics from Animal
