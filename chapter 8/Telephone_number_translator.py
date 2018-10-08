"""
    Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers to remember.
    On a standard telephone the alphabetic letters are mapped to numbers in the following fashion:

    A, B, C = 2

    D, E, F = 3

    G, H, I = 4

    J, K, L = 5

    M, N, O = 6

    P, Q, R, S = 7

    T,U, V, = 8

    W, X, Y, Z = 9

    Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
    The application should display the telephone number with any alphabetic characters that appeared in the
    original translated to their numeric equivalent.
"""

"""
    Constant tables.
"""


alpha = tuple(['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N',
               'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-'])

digits = tuple(['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
                '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '-'])


"""
    Main function. Asks user for phone number with letters in it.
"""


def main():
    number = input("Please enter a phone number (815-EAT-GOOD): ")
    print("Actual number: " + convert_letters_to_numbers(number))


"""
    Converts letters to phone number. Accesses the above tables, gets the index for the character from the first table
    uses that index to find the correct value from the second table.
"""


def convert_letters_to_numbers(letter_phone_number):
    result = ""
    for ch in letter_phone_number.upper():
        index = alpha.index(ch)
        result += digits[index]
    return result


main()
