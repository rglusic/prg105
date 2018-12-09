"""
    Small utility program for producing a 'level' file that the game loads.
"""
import pickle as pk

"""
    Overwrite file each time.
"""


def save_to_file(filename, dictionary):
    try:
        file_ptr = open(filename, 'wb')
        pk.dump(dictionary, file_ptr)
        file_ptr.close()
    except IOError:
        print("Somehow failed to make the file.")


def main():
    level_desc = input("Enter the level description:")
    level_name = input("Enter the level name:")
    level_image = input("Enter the path to the front image:")
    dictionary = {'level_desc': level_desc, 'level_name': level_name, 'level_image': level_image}
    save_to_file("content/level1.dat", dictionary)


main()
