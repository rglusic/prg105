"""
    Write a GUI program that calculates a car’s gas mileage. The program’s window should have Entry widgets that let
    the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on a full tank.
    When a Calculate MPG button is clicked, the program should display the number of miles that the car may be driven
    per gallon of gas. Use the following formula to calculate miles per gallon:

    MPG = miles / gallons

    Make sure you label Entry widgets and results appropriately.
"""
import tkinter

"""
    MilesPerGallon creates a window with two labels, asking the user for the number of miles a car can be driven on per
    tank of gas. It also asks for the total number of gallons of gas it holds. It accepts the two numbers and divides
    them in order to calculate the miles per gallon. The number calculated is them printed to the window.
"""


class MilesPerGallon:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallons_label = tkinter.Label(self.top_frame, text='How many gallons does your car hold?')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=5)

        self.miles_label = tkinter.Label(self.top_frame,  text='How many miles can your car drive on a full tank?')
        self.miles_entry = tkinter.Entry(self.top_frame, width=5)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid_frame, text='Miles Per Gallon:')
        self.mpg_value_label = tkinter.Label(self.mid_frame, textvariable=self.mpg)
        self.mpg_label.pack(side='left')
        self.mpg_value_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        miles = int(self.miles_entry.get())
        gallons = int(self.gallons_entry.get())
        self.mpg.set(format(miles/gallons, '.2f'))


"""
    Instantiates MilesPerGallon.
"""


def main():
    MilesPerGallon()


main()
