"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter


# create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.number_of_rooms = number_of_rooms
        self.square_feet = square_feet
        self.floors = floors

# add the mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.square_feet = square_feet

    def set_floors(self, floors):
        self.floors = floors

# add the accessors for all of  the data attributes
    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_square_feet(self):
        return self.square_feet

    def get_floors(self):
        return self.floors


# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
class SingleFamilyHome(Dwelling):  # pycharm complains if its not camelcase
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        # call the superclass of Dwelling and pass the required arguments, remember to include self
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        # initialize the garage_type and yard_size attributes
        self.garage_type = garage_type
        self.yard_size = yard_size

# create the mutator and accessor methods for the garage_type and yard_size attributes
    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_garage_type(self):
        return self.garage_type

    def get_yard_size(self):
        return self.yard_size


# demonstrate the Single_family_home class, no need to import because you are in the same file
# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods
home = SingleFamilyHome(6, 1200, 1, "Single", .25)


# create the main function
def main():
    print("Number of rooms:", home.get_number_of_rooms())
    print("Square feet:", home.get_square_feet())
    print("floors:", home.get_floors())
    print("garage type:", home.get_garage_type())
    print("acres:", home.get_yard_size())
# call the main function


main()


# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22
class Mammal:
    # The _ _init_ _ method accepts an argument for
    # the mammal's species.
    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message
    # indicating the mammal's species.
    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    def make_sound(self):
        print('Grrr')


# create a Mouse class as a sub class of the mammal class following the Dog example
class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Mouse')

    def make_sound(self):
        print("Squeak squeak")


# create a Bird class as a sub class of the mammal class following the Cat Example
class Bird(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Bird')

    def make_sound(self):
        print("Chirp chirp")


# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created
def main2():
    mammal = Mammal('Regular animal')
    mouse = Mouse()
    bird = Bird()

    print('Here are some animals and')
    print("the sound they make.")
    print("--------------------------")
    show_mammal_info(mammal)
    print()
    show_mammal_info(mouse)
    print()
    show_mammal_info(bird)


def show_mammal_info(animal):
    animal.show_species()
    animal.make_sound()


main2()
