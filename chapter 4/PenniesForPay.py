"""
    Write a program that calculates the amount of money a person would earn over a period of time if his or her salary
    is one penny the first day, two pennies the second day, and continues to double each day. The program should ask
    the user for the number of days. Display a table showing what the salary was for each day, and then show the total
    pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

    Hint: use Range, set the field size in formatting.
"""

total = 0.0
currentValue = 0.01
days = int(input("How many days do you want to work for a penny a day? "))
print("Days Worked | Amount Earned That Day")
print("------------------------------------")

for i in range(1, days+1):
    if i != 1:
        currentValue = currentValue * 2
    print(str(format(i, "10")) + " | $" + str(format(currentValue, "13,.2f")))
    total = total + currentValue

print("Total earned over " + str(days) + " days is $" + str(format(total, "13,.2f")))
