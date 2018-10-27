"""
    Generic employee class. Holds the basic information about an employee.
"""


class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_number(self, number):
        self.number = number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number


"""
    A particular kind of employee which defines the shift and pay of an employee.
"""


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        self.shift = shift
        self.pay = pay

    def get_shift(self):
        if self.shift == 1:
            return "Day"
        else:
            return "Night"

    def get_pay(self):
        return self.pay

    def set_pay(self, pay):
        self.pay = pay

    def set_shift(self, shift):
        self.shift = shift
