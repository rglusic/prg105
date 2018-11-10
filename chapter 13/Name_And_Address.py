"""
    Write a GUI program that displays your name and address when a button is clicked (you can use the address of the
    school). The program’s window should resemble the sketch on the far left side of figure 13-26 when it runs. When
    the user clicks the Show Info button, the program should display your name and address as shown in the sketch on
    the right of the figure.
"""
import tkinter

"""
    NameAndAddress shows the users name and address at the press of a button within a GUI element. The display method
    packs and unpacks the top_frame, which holds the address and name. When display is triggered by the button, the name
    and address is either packed or unpacked from the GUI.
"""


class NameAndAddress:
    def __init__(self):
        self.is_displayed = False
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Ryan Glusic')
        self.descr_label = tkinter.Label(self.top_frame, text='8900 US-14, Crystal Lake, IL 60012')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.display)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def display(self):
        if not self.is_displayed:
            self.prompt_label.pack(side='top')
            self.descr_label.pack(side='top')
            self.is_displayed = True
        else:
            self.prompt_label.pack_forget()
            self.descr_label.pack_forget()
            self.is_displayed = False


"""
    Instantiates the class, creating a window.
"""


def main():
    NameAndAddress()


main()
