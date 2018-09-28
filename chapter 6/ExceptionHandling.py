"""
    Copy your file from the previous exercise (Average numbers) and
    modify it so that it handles the following exceptions:

    It should handle any IOError exceptions that are raised when
    the file is opened and data is read from it.

    It should handle any ValueError exceptions that are raised
    when the items that are read from the file are converted to a number.
"""


"""
    Main function. Calls average_numbers. Stores the return value in a variable and prints it. If average is zero,
    assume that the function failed to open the file.
"""


def main():
    average = average_numbers("numbers2.txt")
    if average != 0:
        print("The average value of the numbers in the file is: " + str(average))


"""
    Opens file, if open fails, returns 0 and prints error message. counts the integers present in the file, adds them
    to a total variable and counts how many there are. Tests values pulled from file to make sure they are a number, 
    Returns an error otherwise and breaks out of the loop. Prints the count and total value. returns the average from 
    the function after formatting to the 100th's place.
"""


def average_numbers(filename):
    try:
        fileptr = open(filename, 'r')
    except IOError:
        print("ERROR, file not present")
        return 0
    total = 0
    count = 0
    for line in fileptr:
        if line.strip():
            try:
                total += int(line)
            except ValueError:
                print("Error, value is not a proper number! Stopping processing of file!")
                break
            count += 1
    print("The count of numbers was: " + str(count))
    print("The total sum was: " + str(format(total, ',')))
    average = format(total / count, ".2f")
    return average


main()
