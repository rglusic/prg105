"""
    A basic entity. A framework for the enemy and player. Uses the simple-audio library for loading and playing sounds
    (MIT licensed).
"""
import pickle
import simpleaudio as sa


class Entity:
    def __init__(self, name, health, level, filename):
        self.health = health
        self.level = level
        self.filename = filename
        self.name = name
        self.table = {}

    def attack(self, description_table, enemy, orientation):
        return 0

    def load_from_file(self):
        try:
            file_ptr = open(self.filename, 'rb')
            self.table = pickle.load(file_ptr)
            self.health = self.table['health']
            self.level = self.table['level']
            file_ptr.close()
        except (FileNotFoundError, IOError):
            file_ptr = open(self.filename, 'wb')
            file_ptr.close()
            self.table = {}

    def save_to_file(self):
        self.table['health'] = self.health
        self.table['level'] = self.level
        try:
            file_ptr = open(self.filename, 'rb')
            pickle.dump(self.table, file_ptr)
            file_ptr.close()
        except (FileNotFoundError, IOError):
            file_ptr = open(self.filename, 'wb')
            file_ptr.close()

    def set_health(self, health):
        self.health = health
        if self.health < 0:
            self.health = 0

    def get_health(self):
        return self.health

    def is_dead(self):
        if self.health == 0:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def set_current_level(self, level):
        self.level = level

    def get_current_level(self):
        return self.level

    @classmethod
    def play_sound_through(cls, filename):
        sa.WaveObject.from_wave_file(filename).play().wait_done()
