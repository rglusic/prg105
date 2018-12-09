"""
    Manages the actions for the players and enemies. Just a way of keeping the GUI class a little cleaner.
"""
from Description import DescriptionManager
from Level import Level


class GameManager:
    def __init__(self, entity_table):
        self.level = Level("content/level1.dat")
        self.level.load_from_file()
        self.description_manager = DescriptionManager(10)
        self.player = entity_table[0]
        index = 0
        self.enemies = []
        for entity in entity_table:
            if index == 0:
                index += 1
                continue
            self.enemies.append(entity)
            index += 1

    def update(self, orientation):
        if self.player.is_dead():
            self.player.play_sound_through("content/sound/failure.wav")
            return "fail"
        self.player.attack(self.description_manager, self.enemies, orientation)

        total_dead = 0
        for e in self.enemies:
            if not e.is_dead():
                e.attack(self.description_manager, self.player, orientation)
            else:
                total_dead += 1
                if total_dead == len(self.enemies):
                    self.player.play_sound_through("content/sound/victory.wav")
                    return "victory"
        return self.description_manager.get_str()

    def get_level(self):
        return self.level
