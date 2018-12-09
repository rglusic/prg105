import tkinter as tk
from PIL import ImageTk, Image
from GameManager import GameManager


"""
    Controls the GUI. It sets up the location of the image, buttons, etc. It lets an instance of a level handle the
    underlying details of what happens (When the user presses a button, the image, etc). Makes use of PIL (Pillow) for
    loading images.
"""


class GameGui:
    def __init__(self, entity_table):
        self.game_manager = GameManager(entity_table)
        self.entity_table = entity_table
        index = 0
        self.enemies = []
        for entity in entity_table:
            if index == 0:
                index += 1
                continue
            self.enemies.append(entity)
            index += 1

        self.window = tk.Tk()
        self.window.title(self.game_manager.get_level().get_level_name())
        self.window.geometry("800x600")

        #  Individual frames for the game.
        self.image_frame = tk.Frame(relief="raised", borderwidth=1)
        self.description_frame = tk.Frame(relief="raised", borderwidth=1)
        self.upper_buttons_frame = tk.Frame()
        self.lower_buttons_frame = tk.Frame()

        #  Load the image and attach it to the canvas. Get path from game manager.
        img = ImageTk.PhotoImage(Image.open(self.game_manager.get_level().get_level_image()))
        image_label = tk.Label(self.image_frame, image=img)
        image_label.image = img
        image_label.pack(side="top", fill="both", expand="true")
        self.image_frame.pack(fill="both", expand=True)

        #  Top variables
        self.image = 0
        self.description = tk.StringVar()
        self.description.set(self.game_manager.get_level().get_level_desc())
        self.description_label = tk.Label(self.description_frame, textvariable=self.description, wraplength=400)
        self.description_label.grid(row=0)
        self.description_frame.pack(fill="both", expand=False)

        #  Buttons in grids.
        self.up_button = tk.Button(self.upper_buttons_frame, text='↑', width=2, command=self.up)
        self.up_button.grid(row=0, column=1)

        self.down_button = tk.Button(self.lower_buttons_frame, text='↓', width=2, command=self.down)
        self.down_button.grid(row=1, column=1)

        self.left_button = tk.Button(self.lower_buttons_frame, text='←', width=2, command=self.left)
        self.left_button.grid(row=1, column=0)

        self.right_button = tk.Button(self.lower_buttons_frame, text='→', width=2, command=self.right)
        self.right_button.grid(row=1, column=2)

        self.yes_button = tk.Button(self.upper_buttons_frame, text='Yes', width=3)
        self.yes_button.grid(row=0, column=3)
        self.no_button = tk.Button(self.upper_buttons_frame, text='No', width=3)
        self.no_button.grid(row=0, column=4)

        #  Pack Buttons and adjust spacing.
        self.upper_buttons_frame.pack()
        self.upper_buttons_frame.grid_columnconfigure(2, minsize=200)
        self.lower_buttons_frame.pack()
        self.lower_buttons_frame.grid_columnconfigure(3, minsize=262)

    def up(self):
        desc_str = self.game_manager.update("up")
        if desc_str == ("victory" or "fail"):
            self.fade_gui()
        else:
            self.description.set(desc_str)

    def down(self):
        desc_str = self.game_manager.update("down")
        if desc_str == ("victory" or "fail"):
            self.fade_gui()
        else:
            self.description.set(desc_str)

    def left(self):
        desc_str = self.game_manager.update("left")
        if desc_str == ("victory" or "fail"):
            self.fade_gui()
        else:
            self.description.set(desc_str)

    def right(self):
        desc_str = self.game_manager.update("right")
        if desc_str == ("victory" or "fail"):
            self.fade_gui()
        else:
            self.description.set(desc_str)

    def fade_gui(self):
        alpha = self.window.attributes("-alpha")
        if alpha > 0:
            alpha -= 0.05
            self.window.attributes("-alpha", alpha)
            self.window.after(100, self.fade_gui)
        else:
            self.window.destroy()

    def run(self):
        self.window.mainloop()
