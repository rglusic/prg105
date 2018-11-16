import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        try:
            input_file = open("customer_file.dat", 'rb')
            customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError, EOFError):
            customers = {}

        #  Just instantiate objects without variables to them, that gets rid of the error Meri was talking about in the
        #  video.
        if self.radio_var.get() == 1:
            LookGUI(self.master, customers)
        elif self.radio_var.get() == 2:
            AddGUI(self.master, customers)
        elif self.radio_var.get() == 3:
            ChangeGUI(self.master, customers)
        else:
            DeleteGUI(self.master, customers)


class LookGUI:
    def __init__(self, master, customers):
        self.customers = customers

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get().lower()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master, customers):
        self.customers = customers
        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.add = tkinter.Toplevel(master)

        self.add.title('Add a customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to add to the database: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.address = tkinter.Label(self.middle_frame, text='Enter customer email address to add to the database: ')
        self.search_entry2 = tkinter.Entry(self.middle_frame, width=15)

        # pack Middle frame
        self.address.pack(side='left')
        self.search_entry2.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Enter', command=self.enter)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def enter(self):
        # open the file, load to customers, close file. Do in each class
        try:
            out_file = open("customer_file.dat", 'wb')
        except (FileNotFoundError, IOError):
            print("Error, cant open file.")
            self.add.quit()
            return  # Here for the IDE to stop complaining

        self.customers[self.search_entry.get().lower()] = self.search_entry2.get()
        pickle.dump(self.customers, out_file)
        out_file.close()

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master, customers):
        self.customers = customers

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Change customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.search_label2 = tkinter.Label(self.middle_frame, text='Enter the new email for the customer: ')
        self.search_entry2 = tkinter.Entry(self.middle_frame, width=15)

        # pack Middle frame
        self.search_label2.pack(side='left')
        self.search_entry2.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Change', command=self.change)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def change(self):
        # open the file, load to customers, close file. Do in each class
        try:
            output = open("customer_file.dat", 'wb')
        except (FileNotFoundError, IOError):
            print("File does not exist, nothing to change")
            self.look.quit()
            return  # Here to stop the IDE from complaining.

        name = self.search_entry.get().lower()
        if name in self.customers:
            self.customers[name] = self.search_entry2.get()

        pickle.dump(self.customers, output)
        output.close()

    def back(self):
        self.look.destroy()


class DeleteGUI:
    def __init__(self, master, customers):
        self.customers = customers

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError, EOFError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Delete customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def delete(self):
        # open the file, load to customers, close file. Do in each class
        try:
            output = open("customer_file.dat", 'wb')
        except (FileNotFoundError, IOError):
            print("File does not exist, nothing to change")
            self.look.quit()
            return  # Here to stop the IDE from complaining.

        name = self.search_entry.get().lower()
        if name in self.customers:
            del self.customers[name]

        pickle.dump(self.customers, output)
        output.close()

    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
