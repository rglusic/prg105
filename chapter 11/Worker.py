"""
    File 1:

    Write an Employee class that keeps data attributes for the following pieces of information:

    Employee name
    Employee number
    Next, Write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class
    should keep data attributes for the following information

    Shift numbered (an integer, such as 1, 2, or 3)
    Hourly pay rate
    The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing
    the shift that the employee works. The day shift is shift 1 and the night shift is shift 2. Write the appropriate
    accessor and mutator methods (get and set) for each class.

    File 2:

    Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts
    the user to enter data for each of the object’s data attributes. Store the data in the object and then use the
    object’s accessor methods to retrieve it and display it on the screen.
"""
import Employee


"""
    Instantiates a ProductionWorker object, asks the user to enter the details to do so. Prints out the details 
    afterwards.
"""


def main():
    print("Enter the following details of the employee")
    print("--------------------------------------------------------")
    name = input("Enter the employee name: ")
    number = input("Enter the employee number: ")
    pay = float(input("Enter the employee pay: "))
    shift = int(input("Enter the employee shift: "))
    ryan = Employee.ProductionWorker(name, number, shift, pay)
    print("--------------------------------------------------------")
    print("Details of the employee:")
    print("--------------------------------------------------------")
    print("Name: " + ryan.get_name())
    print("Employee Number: " + ryan.get_number())
    print("Shift: " + ryan.get_shift())
    print("Pay rate: $" + str(ryan.get_pay()))


main()
