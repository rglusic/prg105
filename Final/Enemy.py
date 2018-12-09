"""
    Houses enemy class. Derived from entity. The enemy is the enemy the player faces.
"""
from Entity import Entity
import random as rand


class Enemy(Entity):
    def __init__(self, name, health, level, filename):
        Entity.__init__(self, name, health, level, filename)

    def attack(self, description_table, e, orientation):
        chance = rand.randint(0, 100)
        if chance > 25:
            damage = rand.randint(1, 10)
            e.set_health(e.get_health()-damage)
            description_table.append("Ouch, the enemy hit you! (" + str(damage) + " damage dealt)")
            self.play_sound_through("content/sound/enemyhit.wav")
        elif chance < 10:
            self.health -= 1
            description_table.append("This enemy failed so bad they hurt themselves (" + str(self.health) +
                                     " health)")
            self.play_sound_through("content/sound/hurtthemselves.wav")
        else:
            description_table.append("The enemy missed")
            self.play_sound_through("content/sound/enemymiss.wav")
