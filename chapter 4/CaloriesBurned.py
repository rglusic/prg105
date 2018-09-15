"""
    Running on a treadmill you burn 4.2 calories per minute.
    Write a program that uses a loop to display the number of
    calories burned after 10, 15, 20, 25 and 30 minutes.
"""

burned = 4.2

for time in [10, 15, 20, 25, 30]:
    print("Burned " + str(burned*time) + " Calories after " + str(time) + " minutes.")
