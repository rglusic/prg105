"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module

# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter

# create the class MyGUI2


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        tkinter.mainloop()


my_gui = MyGUI()

# TODO 13.3 Adding a label widget
# add a label that prints your first and last name


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Ryan Glusic')

        # pack the label
        self.label.pack()
        # enter the main loop
        tkinter.mainloop()


# create an instance of MyGUI2

my_gui2 = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
# Create a window in the MyGUI3 class that has two frames
# In the top Frame add a labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Ryan Glusic')
        self.label2 = tkinter.Label(self.top_frame, text='BS in Physics')
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        self.label3 = tkinter.Label(self.bottom_frame, text='Calc III')
        self.label4 = tkinter.Label(self.bottom_frame, text='Physics II')
        self.label5 = tkinter.Label(self.bottom_frame, text='Logic Programming')
        self.label6 = tkinter.Label(self.bottom_frame, text='Film')
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.label6.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box


class MyGUI4:
    def __init__(self):
        self.joke = "Because he wanted to."
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Why did the chicken cross the road?')
        self.label.pack()
        self.the_button = tkinter.Button(self.main_window, text='Why?', command=self.tell_joke)
        self.the_button.pack()
        tkinter.mainloop()

    def tell_joke(self):
        tkinter.messagebox.showinfo('Joke', self.joke)


my_gui4 = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters


class MyGUI5:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter the measured inches:')
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to centimeters:')
        self.value = tkinter.StringVar()
        self.centi_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.descr_label.pack(side='left')
        self.centi_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        centi = inch*2.54
        self.value.set(centi)


my_gui5 = MyGUI5()
