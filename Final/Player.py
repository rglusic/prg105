"""
    This file houses the player class. The player class keeps track of everything that involves the player. It also
    contains an instance of a class that lets it save or load its information to a file. Inherits Entity class.
"""
import random as rand
from Entity import Entity


class Player(Entity):
    def __init__(self, health, level, filename):
        Entity.__init__(self, "Player", health, level, filename)

    def attack(self, description_table, entity_table, orientation):
        if orientation == "up":
            description_table.append("You slash your sword upwards")
        elif orientation == "down":
            description_table.append("You slash your sword downwards")
        elif orientation == "left":
            description_table.append("You slash your sword left")
        elif orientation == "right":
            description_table.append("You slash your sword right")

        for e in entity_table:
            if not e.is_dead():
                chance = rand.randint(0, 100)
                if chance > 25:
                    damage = rand.randint(1, 10)
                    e.set_health(e.get_health()-damage)
                    description_table.append("Take that " + e.get_name() + "! (" + str(damage) + " damage dealt)")
                    self.play_sound_through("content/sound/enemyhit.wav")
                elif chance < 10:
                    self.health -= 1
                    description_table.append("Ouch, you failed and hurt yourself. Good job. (" + str(self.health) +
                                             " health)")
                    self.play_sound_through("content/sound/hurtthemselves.wav")
                else:
                    description_table.append("You missed")
                    self.play_sound_through("content/sound/enemymiss.wav")
