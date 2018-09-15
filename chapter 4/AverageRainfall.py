"""
    Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
    The program should first ask for the number of years. The outer loop will iterate once for each year.
    The inner loop will iterate 12 times, once for each month. Each iteration of the inner loop will ask the user for
    the inches of rainfall for that month. After all iterations, the program should display the number of months,
    the total inches of rainfall, and the average rainfall per month for the entire period.
"""

years = int(input("How many years would you like to enter data for? "))
total_inches = 0
month_table = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

for i in range(1, years+1):
    print("Year " + str(i))
    for j in month_table:
        inches = int(input("Inches of rainfall for month of " + j + "? "))
        total_inches = total_inches + inches

print("The total number of months: " + str(years*12))
print("The total rainfall was: " + str(format(total_inches, ",.2f")) + " inches")
print("The average rainfall per month was: " + str(format(total_inches / (years*12), ",.2f")) + " inches")
