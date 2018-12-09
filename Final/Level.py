"""
    This file contains the Level class. The purpose of the Level class is to handle which level is currently running
    and to keep track of all it's state. Passes its state down in the game manager class.
"""
import pickle


class Level:
    def __init__(self, filename):
        self.filename = filename
        self.level_desc = ""
        self.level_name = ""
        self.level_image = ""
        self.table = {}

    def load_from_file(self):
        try:
            file_ptr = open(self.filename, 'rb')
            self.table = pickle.load(file_ptr)
            self.level_desc = self.table['level_desc']
            self.level_name = self.table['level_name']
            self.level_image = self.table['level_image']
            file_ptr.close()
        except (FileNotFoundError, IOError):
            print("Error, file doesn't exist!")

    def get_level_desc(self):
        return self.level_desc

    def get_level_name(self):
        return self.level_name

    def get_level_image(self):
        return self.level_image
