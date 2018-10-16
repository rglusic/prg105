"""
    Write a program that keeps names and email addresses in a dictionary as key-value pairs.
    The program should display a menu that lets the user look up a person's email address,
    add a new name and email address, change an existing email address, and delete an existing
    name and email address. The program should pickle the dictionary and save it to a file when
    the user exits the program. Each time the program starts, it should retrieve the dictionary
    from the file and unpickle it.
"""
import pickle

"""
    Main function. Call's menu function.
"""


def main():
    menu()


"""
    Retrieves dictionary from file using pickle library. Returns it. If file cannot be opened, assume it doesn't
    exist and create a new one.
"""


def retrieve_dict(filename):
    try:
        file_ptr = open(filename, 'rb')
    except IOError:
        file_ptr = open(filename, 'wb')
        file_ptr.close()
        return {}
    dictionary = pickle.load(file_ptr)
    file_ptr.close()
    return dictionary


"""
    Saves dictionary to file using pickle.
"""


def save_dict(filename, dictionary):
    try:
        file_ptr = open(filename, 'wb')
    except IOError:
        print("Cannot open file for writing")
        return -1
    pickle.dump(dictionary, file_ptr)
    file_ptr.close()
    return 0


"""
    Menu that handles overseering the dictionary. Allows the user to enter items into, reads and update
    the dictionary. On exit command, saves dictionary to file and breaks out of the loop.
"""


def menu():
    print("--- Name and Email Address' Menu ---")
    dictionary = retrieve_dict("Emails.bin")
    print("Current entries in database: " + str(dictionary.items()))
    while True:
        option = input("Options:\na) Add/Update address\nr) Remove address\nl) list address\ne) exit\n").lower()
        if option == 'a':
            print("--- Adding/Updating entry ---")
            key = input("Please enter the name: ").lower()
            value = input("Please enter the email: ").lower()
            add_entry(dictionary, key, value)
        elif option == 'r':
            print("--- Deleting entry ---")
            key = input("Please enter the name: ").lower()
            remove_entry(dictionary, key)
        elif option == 'l':
            print("--- Listing address ---")
            key = input("Please enter the name: ").lower()
            list_entry(dictionary, key)
        elif option == 'e':
            print("--- Exiting ---")
            save_dict("Emails.bin", dictionary)
            break


"""
    Adds or updates entry in dictionary.
"""


def add_entry(dictionary, key, value):
    dictionary[key] = value


"""
    removes entry from dictionary.
"""


def remove_entry(dictionary, key):
        if key in dictionary:
            del dictionary[key]


"""
    list entry in dictionary.
"""


def list_entry(dictionary, key):
        if key in dictionary:
            print("Email address of " + key + " is: " + dictionary[key])
        else:
            print("No one by that name in the database. Did you enter the full name?")


main()
