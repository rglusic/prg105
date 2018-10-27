"""
    In the first step, you will create a parent class. Create a parent class for Office Furniture. Set the class
    variables to be a category (desk, chair, filing cabinet would be examples), material, length, width, height, and
    price. Include a method that returns a string about the object.

    In the second step create a subclass for Desk that includes location_of_drawers (left, right both are options) and
    number_drawers. Override the parents __str__ method to include drawer location and count.

    Implement each class in a separate file. Import these into your main program. Your main program should implement
    and display an instance of each, the parent class and the child class.
"""
import Office_Furniture
import Desk

"""
    Creates an instance of the OfficeFurniture class. Used to describe a chair.
    Creates an instance of the Desk class, which inherits OfficeFurniture. Describes a desk.
    Calls each describe version.
"""


def main():
    chair = Office_Furniture.OfficeFurniture('Office chair', 'plastic', '2 ft', '2 ft', '5 ft', '$300')
    desk = Desk.Desk('Oak', '5 ft', '7 ft', '9 ft', '$5,000', 'left', '2')
    chair.describe()
    desk.describe()


main()
