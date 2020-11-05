from reptile import Reptile


# Creating a Snake class as a child class of Reptile
class Snake(Reptile):
    #  Initialising the Snake class, and using super() also use the initialise method in Reptile
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True

    # Creating methods for our Snake class
    def use_tongue(self):
        return "Use your tongue to find prey"


# nagini = Snake()  # Instantiating an object of the Snake class
# print(nagini.venom)  # Has access to all of it's class functions and attributes
# print(nagini.use_tongue())
# print(nagini.cold_blooded)  # Also has access to attributes from Reptile, the parent class
# print(nagini.breathe())  # And can ALSO access things from Animal, the Parent of Reptile
