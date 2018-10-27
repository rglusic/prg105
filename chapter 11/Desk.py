import Office_Furniture

"""
    Describes a desk while inheriting the Office furniture class.
"""


class Desk(Office_Furniture.OfficeFurniture):
    def __init__(self, material, length, width, height, price, location_of_drawers, number_drawers):
        Office_Furniture.OfficeFurniture.__init__(self, "Office desk", material, length, width, height, price)
        self.location_of_drawers = location_of_drawers
        self.number_drawers = number_drawers

    def describe(self):
        print(str(self.category) + " made of " + str(self.material) + ", with a length of " + str(self.length) + " by " +
              str(self.width) + " wide and a height of " + str(self.height) + ". It has " + str(self.number_drawers) +
              " drawers on the " + str(self.location_of_drawers) + " side with a price of " + str(self.price))
