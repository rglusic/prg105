"""
    Read and Display the list of names from the file
    Display the number of names that are read from the file
    (You will need a variable to keep a count of the number of items read from the file.)
"""


"""
    Calls readfile function. Stores return value as variable, then prints it.
"""


def main():
    number_of_names = readfile("names.txt")
    print("There are a total of " + str(number_of_names) + " names in the file.")


"""
    Attempts to open the file, prints error if it cant. Reads each line in the file, prints them and increments
    a counter for each line present, which it later returns. Ignores any whitespace lines present.
"""


def readfile(filename):
    try:
        fileptr = open(filename, 'r')
    except IOError:
        print("ERROR, file not present.")
        return 0
    count = 0
    for line in fileptr:
        if line.strip():  # Strips whitespace from line. If line only has whitespace, returns false
            count += 1
            print(line)
    return count


main()
