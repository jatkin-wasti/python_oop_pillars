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


# Creating an object of our Reptile class to utilise the OOP functionalities
# reptile_object = Reptile()
# print(reptile_object.move())  # It can access this method from the Animal (Parent) class through inheritance
# print(reptile_object.seek_heat())  # While also having all of the functionality of the Reptile class
