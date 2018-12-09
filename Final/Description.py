"""
    Manages the description for the GUI. Just a wrapper for a list. Ease of integration with GUI, Player and Enemy.
    Returns a string of the array.
"""


class DescriptionManager:
    def __init__(self, max_elements):
        self.description_table = []
        self.max_elements = max_elements

    def append(self, text):
        if self.max_elements == len(self.description_table):
            self.description_table.pop(0)

        self.description_table.append(text)

    def get_str(self):
        new_str = ""
        for txt in self.description_table:
            new_str += txt + "\n"
        return new_str
