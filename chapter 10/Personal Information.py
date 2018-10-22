"""
    Design a class that holds the following personal data: name, address, age, and phone number.
    Write appropriate accessor and mutator methods (get and set). Write a program that creates three
    instances of the class. One instance should hold your information and the other two should hold
    your friends or family members' information.  Just add information, don't get it from the user.
    Print the data from each object, make sure to format the output for clarity and ease of reading.

    For this assignment, a class diagram is provided for you. In future assignments, you will have to
    plan your own project using class diagrams, do this using word and a single column table.
    The video also explains what accessors and mutators are.
"""

"""
    This classes houses the name, address, age and phone number of a person. It has setter and getter methods to
    set and retrieve the information.
"""


class PersonalData:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0
        self.phone = ""

    def set_name(self, person_name):
        self.name = person_name

    def set_address(self, person_address):
        self.address = person_address

    def set_age(self, person_age):
        self.age = person_age

    def set_phone(self, person_phone):
        self.phone = person_phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


"""
    Main function. Creates three instances of PersonalData and assigns information to them. Prints the results.
"""


def main():
    ryan = PersonalData()
    ryan.set_name("Ryan Glusic")
    ryan.set_address("Wright Rd. McHenry")
    ryan.set_age(22)
    ryan.set_phone("815-701-7036")

    john = PersonalData()
    john.set_name("John Doe")
    john.set_address("Someplace 123 Ave")
    john.set_age(72)
    john.set_phone("815-432-1111")

    jane = PersonalData()
    jane.set_name("Jane Doe")
    jane.set_address("SomeOtherPlace 123 Ave")
    jane.set_age(24)
    jane.set_phone("847-111-1111")

    print("---------------------")
    print(ryan.get_name() + "\n" + str(ryan.get_age()) + "\n" + ryan.get_address() + "\n" + ryan.get_phone())
    print("---------------------")
    print(john.get_name() + "\n" + str(john.get_age()) + "\n" + john.get_address() + "\n" + john.get_phone())
    print("---------------------")
    print(jane.get_name() + "\n" + str(jane.get_age()) + "\n" + jane.get_address() + "\n" + jane.get_phone())


main()
