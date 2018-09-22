"""
    A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation,
    she asks members for the number of fat grams, carbohydrate grams, and protein grams that they consumed in a day.
    Then, she calculates the number of calories that result from the fat, using the following formula:

    calories from fat = fat grams X 9

    Next, she calculates the number of calories that result from the carbohydrates, using the following formula:

    calories from carbs = carb grams X 4

    Next, she calculates the number of calories that result from the proteins, using the following formula:

    calories from protein = protein grams X 4



    Use a different function for each nutrient to make calculations by nutrient,
    and print the calories for that nutrient on screen.
    Return the results from each function to variables in the main method.
    Add the variables in the main method to display the total calories for the day.
    Use meaningful names for each variable and function. Add a comment to each function describing what it does.
"""


"""
    Asks the user to input their amount of fat, carbs and proteins they consumed today. Calculates the
    Calories from those inputs and prints out the individual calories due to each one. Finally, calculates
    the total amount of Calories consumed and prints it.
"""


def main():
    calories_from_fat = fat(int(input("How many grams of fat did you eat today? ")))
    print("You ate a total of " + str(format(calories_from_fat, ",")) + " Calories from fat today.")

    calories_from_carbs = carbs(int(input("How many grams of carbs did you eat today? ")))
    print("You ate a total of " + str(format(calories_from_carbs, ",")) + " Calories from carbs today.")

    calories_from_proteins = protein(int(input("How many grams of protein did you eat today? ")))
    print("You ate a total of " + str(format(calories_from_proteins, ",")) + " Calories from protein today.")

    total = calories_from_fat + calories_from_carbs + calories_from_proteins
    print("You ate a total of " + str(format(total, ",")) + " Calories today.")


"""
    Calculates the amount of calories per grams of fat, and returns the result.
"""


def fat(fat_mass):
    return fat_mass * 9


"""
    Calculates the amount of calories per grams of carbs, and returns the result.
"""


def carbs(carb_mass):
    return carb_mass * 4


"""
    Calculates the amount of calories per grams of protein, and returns the result.
"""


def protein(protein_mass):
    return protein_mass * 4


"""
    Runs the program.
"""
main()
