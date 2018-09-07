"""
    The user provides a number 1 - 7. The program displays which day that corresponds to. If the user enters a number
    out of this range, the program reports an error.
"""

number = int(input("Give a number between 1 and 7 "))

if number == 1:
    print("The day is Monday.")
elif number == 2:
    print("The day is Tuesday.")
elif number == 3:
    print("The day is Wednesday.")
elif number == 4:
    print("The day is Thursday.")
elif number == 5:
    print("The day is Friday.")
elif number == 6:
    print("The day is Saturday.")
elif number == 7:
    print("The day is Sunday.")
else:
    print("Number is not between 1 and 7.")
