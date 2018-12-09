"""
    The main file of the final project. This is where everything is instantiated from their respective classes and
    executed. Main game loop as well.
"""
from GUI import GameGui
from Player import Player
from Enemy import Enemy


def main():
    entity_table = [Player(100, 0, "player.dat"), Enemy("Knight", 15, 0, "boss.dat"), Enemy("Guard", 15, 0, "boss2.dat")]
    game = GameGui(entity_table)
    game.run()


main()
