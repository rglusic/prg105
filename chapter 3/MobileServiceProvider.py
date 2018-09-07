"""
    Write a program that calculates a customer's monthly bill. It should ask which package the customer
    has purchased and how many minutes were used. It should then display the total amount due.
    Use a dollar sign and two decimal places for currency.
"""

packageAString = "Package A: For $39.99 per month, 450 minutes are provided. Additional minutes are $0.45 per minute."
packageBString = "Package B: For $59.99 per month, 900 minutes are provided. Additional minutes are $0.40 per minute."
packageCString = "Package C: For $69.99 per month, unlimited minutes provided."

packageAMinutes = 450
packageAPrice = 39.99

packageBMinutes = 900
packageBPrice = 59.99

PackageCPrice = 69.99

print(packageAString)
print(packageBString)
print(packageCString + '\n')

user_package = input("What package do you have? (A, B, C): ")
user_package = user_package.lower()  # Don't need an or statement now in my ifs.

if user_package == 'a':
    price = 39.99
    user_minutes = int(input("How many minutes have you used this month? "))
    overcharge = user_minutes-450
    if overcharge > 0:
        price = price + 0.45*overcharge
    print("Your bill this month is: $" + str(format(price, ',.2f')))
elif user_package == 'b':
    price = 59.99
    user_minutes = int(input("How many minutes have you used this month? "))
    overcharge = user_minutes-900
    if overcharge > 0:
        price = price + 0.40*overcharge
    print("Your bill this month is: $" + str(format(price, ',.2f')))
elif user_package == 'c':
    price = 69.99
    print("Your bill this month is: $" + str(format(price, ',.2f')))
else:
    print("You did not pick A, B, or C.")
