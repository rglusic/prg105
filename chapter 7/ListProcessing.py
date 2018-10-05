"""
    1. Have a function that creates a list of 20 random integers between 1 and 100
    (Assign them dynamically, store the list in a variable.)

    2. Have a function get a number from the user that is between 1 and 100
    (validate to ensure a number between 1 and 100 was entered instead of text or
    something out of range using a try and except statement).

    3. Pass both the list and the user's number to a function and have it display
    all numbers in the list that is greater than the user's number. If there are not any,
    display a message that explains there are no numbers in the list greater than the entered number.
"""
import random


"""
    Calls all the functions necessary for the program.
"""


def main():
    rand = random_list()
    user_number = get_user_number()
    number_compare(rand, user_number)


"""
    Creates a list of 20 random integers between 1 and 100. Returns the list.
"""


def random_list():
    rand_list = []
    for i in range(1, 21):
        rand_list.append(random.randint(1, 100))
    return rand_list


"""
    Gets a number from the user. Validates to make sure they entered a number between 1 and 100.
"""


def get_user_number():
    while True:
        try:
            num = int(input("Please enter a number between 1 and 100. "))
            if (num < 1) or (num > 100):
                print("Your number is not between 1 and 100.")
            else:
                return num
        except ValueError:
            print("Error, not a number.")


"""
    Takes a list of numbers and another number. Compares the two and prints out all the numbers in the list that are
    greater than the other number. If there aren't any, prints out that there aren't any.
"""


def number_compare(number_list, input_number):
    count = 0
    for num in number_list:
        if num > input_number:
            count += 1
            print(num)
    if count == 0:
        print("There weren't any numbers greater in the list than what was entered.")


main()
