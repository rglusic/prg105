"""
    Write a program that gets a string from the user containing a person's first, middle, and last names and
    then displays their first, middle, and last initials.  (Creating a new variable and concatenating each letter
    plus a '.' is the easiest way to do this.)
"""


"""
    Requests users name. Splits it into a list, grabs first letter from each split, concatenates them into one var
    with a ., finally prints the result.
"""


def main():
    name_list = input("Please enter your full name (first, middle and last) ").split()
    initial = ''
    for name in name_list:
        initial += name[0] + '.'
    print("Your name's initials are: " + initial.upper())


main()
