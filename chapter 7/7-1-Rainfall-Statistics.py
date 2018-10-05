"""
    Copy program 4.3 into the chapter 7 folder and rename it as "7-1-Rainfall-Statistics"

    Modify the program so that the rainfall for each month is stored into a list. Eliminate the user's ability
    to select the number of years, you will just work with one year's data.   The program should calculate and
    display the total rainfall for the year, the average monthly rainfall the year, and the months with the
    highest and lowest amounts of rain for the year. Hint: convert months to a list so you can use the index
    value to print the max and min months.
"""


"""
    Immutable global list for months.
"""
month_table = tuple(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                     "November", "December"])


"""
    Calls calc_rainfall and uses the array it returns to calculate the total rainfall, and average over a year.
    Calculates the min and max rainfall, and their associated months. Prints all of them.
"""


def main():
    rainfall_list = calc_rainfall()
    total = sum(rainfall_list)
    max_rain = max(rainfall_list)
    min_rain = min(rainfall_list)
    max_rain_month = month_table[rainfall_list.index(max_rain)]
    min_rain_month = month_table[rainfall_list.index(min_rain)]

    print("The total rainfall was " + str(format(total, ",.2f")) + " inches")
    print("The average rainfall per month was " + str(format(total / 12, ",.2f")) + " inches")
    print("The month with the highest rainfall was " + max_rain_month + " at a total of " + str(max_rain) + " inches")
    print("The month with the lowest rainfall was " + min_rain_month + " at a total of " + str(min_rain) + " inches")


"""
    Calculates the total rainfall within a year, by iterating over a loop for which the user enters the rainfall per
    month. The result is stored in an array and returned.
"""


def calc_rainfall():
    month_rainfall = []
    for j in month_table:
        month_rainfall.append(int(input("Inches of rainfall for month of " + j + "? ")))
    return month_rainfall


main()
