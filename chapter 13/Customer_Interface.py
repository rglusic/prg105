"""
    Make up an interface for a business offering 7-10 services or products with prices. Write a GUI program to allow the
    user to click buttons to add services or products and show total at the bottom. Make sure all necessary labels and
    instructions to the user are included in your GUI.

    Possibilities: Garage, Salon, Coffeeshop, etc...
"""
import tkinter

"""
    This class creates a GUI for which the user can pick and choose which repairs or replacements they need for their
    car. The checkboxes they choose hold different values which are used to calculate the total price, once the user
    clicks the calculate total button. The buttons values are stored in a 2D array and are created by using said array.
"""


class CustomerInterface:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.questions_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.answer_frame = tkinter.Frame()
        self.prices_array = [125, 75, 35, 350, 300, 75, 25]
        self.buttons = [["New brakes? $125", tkinter.IntVar()], ["New battery? $75", tkinter.IntVar()],
                        ["New lights? $35", tkinter.IntVar()], ["New airbags? $350", tkinter.IntVar()],
                        ["New paint? $300", tkinter.IntVar()], ["New rotors? $75", tkinter.IntVar()],
                        ["Oil change? $25", tkinter.IntVar()]]

        self.intro = tkinter.Label(self.top_frame, text='Welcome to Ryan\'s Garage Application. Here is where you can'
                                                        '\ncalculate how much everything you need for your '
                                                        'car will cost!',
                                   padx=15)
        self.intro.pack(side='top')

        for text, var in self.buttons:
            new_button = tkinter.Checkbutton(text=text, variable=var)
            new_button.pack(side='bottom')

        self.calc_button = tkinter.Button(self.button_frame, text='Calculate total', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.total = tkinter.StringVar()
        self.total_label = tkinter.Label(self.answer_frame, text='Total:')
        self.total_value_label = tkinter.Label(self.answer_frame, textvariable=self.total)
        self.total_label.pack(side='left')
        self.total_value_label.pack(side='left')

        self.top_frame.pack()
        self.questions_frame.pack()
        self.button_frame.pack()
        self.answer_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        total_calc = 0
        index = 0
        for _, val in self.buttons:
            if val.get():
                total_calc += self.prices_array[index]
            index += 1
        self.total.set(str("$" + str(total_calc)))


"""
    Instantiates CustomerInterface.
"""


def main():
    CustomerInterface()


main()
