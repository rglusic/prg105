"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0 (While num > 0)


num = 10
# write your code here, the variable needs to exist before
# you test it
while num > 0:
    num = num - 1
print(num)

# TODO 4.3 the For Loop
# Use a for loop with a list of the days of the week, print each day
# of the week
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print(day)

# TODO 4.3 the for loop - range function
# use the range function to print the numbers from 1 to 10
for num in range(1, 10):
    print(num)

# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers
total = 0
for count in range(5):
    total = total + int(input("Enter a number: "))
print("The total is: " + str(total))

# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the average (total / count)
total = 0
count = 0
sentinel = -1
number = float(input("Please enter a test score: "))
while number != sentinel:
    count += 1
    total += number
    number = float(input("Please enter a test score: "))

print("The total score: " + str(total) + ", the count of scores: " + str(count) + ", and the average: "
      + str(total/count))

# TODO 4.6 validating data
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data
number = int(input("Please enter a number between 1 and 10: "))
while (number < 1) or (number > 10):
    print("ERROR: That number was not between 1 and 10.")
    number = int(input("Please enter a number between 1 and 10: "))
print("The number entered was: " + str(number))
