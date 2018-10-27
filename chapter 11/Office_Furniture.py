"""
    Describes office furniture. Used as a base class. Has a method which prints out the different aspects of the office
    furniture.
"""


class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def describe(self):
        print(str(self.category) + " made of " + str(self.material) + ", with a length of " + str(self.length) + " by " +
              str(self.width) + " wide and a height of " + str(self.height) + " with a price of " + str(self.price))
