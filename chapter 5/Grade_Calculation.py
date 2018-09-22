"""
    Write a program that asks a user to enter five test scores.
    You will need to create five variables to hold these scores.

    The purpose of this assignment is to get practice passing information between functions,
    this is not a good example of the way programs are really written,
    but it will help you to understand how to pass parameters.
"""

"""
    Asks the user for five test grade scores. Calls the calc_average function to calculate the average
    of the scores, then prints it out. Passes the average score to the determine_grade function, 
    which determines the letter grade of the average score and stores the letter in a variable. 
    Prints the letter grade from the variable.
"""


def main():
    score1 = float(input("Enter a test score (1/5): "))
    score2 = float(input("Enter a test score (2/5): "))
    score3 = float(input("Enter a test score (3/5): "))
    score4 = float(input("Enter a test score (4/5): "))
    score5 = float(input("Enter a test score (5/5): "))

    average = calc_average(score1, score2, score3, score4, score5)
    print("The average is: " + str(average))

    grade_letter = determine_grade(average)
    print("Final Grade: " + grade_letter)


"""
    Calculates the average of five grades that were entered. Returns it as a result.
"""


def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5


"""
    Calculates the letter grade based on the value of the input. Returns a letter of the corresponding grade.
    I'm making an assumption that greater than 100 is an A.
"""


def determine_grade(average):
    if average >= 90:
        return "A"
    elif (average >= 80) and (average < 90):
        return "B"
    elif (average >= 70) and (average < 80):
        return "C"
    elif (average >= 60) and (average < 70):
        return "D"
    elif average < 60:
        return "F"


"""
    Runs the program.
"""
main()
