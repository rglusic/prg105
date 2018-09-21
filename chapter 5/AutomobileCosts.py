"""
    Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his
    or her automobile: loan payment, insurance, gas, and maintenance. The program should then display the total monthly
    cost of these expenses, and the total annual cost of these expenses.

    Assign meaningful names to your functions and variables. Every function also needs a comment explaining
    what it does and what other function it works with.
"""

"""
    Calls the other functions. Passes total monthly cost to yearly cost.
"""


def main():
    total = monthly()
    yearly(total)


"""
    Asks the user how much they spend monthly on their loan, insurance and gas for their car.
    Adds the values up into a total and prints it, finally returning it in order to use it
    in another function.
"""


def monthly():
    loan = float(input("How much do you pay for your car loan each month? "))
    insurance = float(input("How much do you pay for your car insurance each month? "))
    gas = float(input("How much do you spend on gas each month? "))
    maintenance = float(input("How much do you spend on the maintenance of your car a month? "))

    total = loan + insurance + gas + maintenance
    print("You pay a total of $" + format(total, ",.2f") + " on your car each month.")
    return total


"""
    Calculates the total price annually by passing in the price monthly. Prints out the price spent each year. 
"""


def yearly(monthly_total):
    yearly_total = monthly_total * 12
    print("You pay a total of $" + format(yearly_total, ",.2f") + " on your car each year")


"""
    Runs the program.
"""
main()
