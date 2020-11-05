from snake import Snake


# Creating a python class as child of our Snake class
class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    # Defining methods for the Python class
    def digest_large_prey(self):
        return "Yum"

    def climb(self):
        return "Onward and upwards"

    def shed_skin(self):
        return "Feeling fresh"


# new_python = Python()  # Creating an object of our Python class
# print(new_python.shed_skin())  # Showing functionality from the Python class
# print(new_python.forked_tongue)  # Showing an attribute from the Snake class
# print(new_python.tetrapod)  # Showing an attribute from the Reptile class
# print(new_python.breathe())  # Showing functionality from the Animal class
# We have access to attributes and functionality from throughout the entire inheritance list!
