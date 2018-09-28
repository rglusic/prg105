"""
    Write a program that uses the numbers.txt file, which contains a series of integers.
    Your program will calculate the average of all of the numbers stored in the
    file and display the total on the screen. Format to show a maximum of two
    numbers to the right of the decimal point.
"""


"""
    Main function. Calls average_numbers. Stores the return value in a variable and prints it.
"""


def main():
    average = average_numbers("numbers.txt")
    print("The average value of the numbers in the file is: " + str(average))


"""
    Opens file, if open fails, returns 0 and prints error message. counts the integers present in the file, adds them
    to a total variable and counts how many there are. Prints the count and total value. returns the average from 
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
            total += int(line)
            count += 1
    print("The count of numbers was: " + str(count))
    print("The total sum was: " + str(format(total, ',')))
    average = format(total / count, ".2f")
    return average


main()
