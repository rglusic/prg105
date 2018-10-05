"""
    Write a program that reads the contents of the two files into two separate lists.
    The user should be able to enter a boy's name or a girl's name. The application should check both lists,
    and then display messages indicating whether the names were among the most popular if the name was on
    one of the lists or that the name was not on the lists of popular names.
"""


"""
    Stores contents of popular names for boys and girls into their own lists. Asks the user for a name, and checks if
    the name is among the popular names.
"""


def main():
    boys_list = read_into_list("BoyNames.txt")
    girls_list = read_into_list("GirlNames.txt")
    name = input("Please enter a name: ").lower()
    if name in boys_list:
        print("It's a popular boy name!")
    elif name in girls_list:
        print("It's a popular girl name!")
    else:
        print("It's not popular at all.")


"""
    Reads the contents the file into a list. Strips the newline terminators. Returns the list
    as a tuple, as it's data should remain constant. Makes all names lowercase for easier compare later.
"""


def read_into_list(filename):
    try:
        file_ptr = open(filename, 'r')
    except IOError:
        print("Error, can't open file.")
        return 0
    file_list = file_ptr.readlines()
    file_ptr.close()

    index = 0
    for line in file_list:
        file_list[index] = line.rstrip('\n')
        file_list[index] = file_list[index].lower()
        index += 1
    return tuple(file_list)


main()
