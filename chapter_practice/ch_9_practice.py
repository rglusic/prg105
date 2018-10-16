"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import pickle
# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14', 'Mary': 'May 12', 'Ryan': 'Jan 6', 'John': 'Mar 2'}

# 1.Print Meri's Birthday
print("Meri's birthday: " + birthdays['Meri'])
# 2.Create an empty dictionary named registration
registration = {}
# 3.You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop
for key in miles_ridden:
    print(key, miles_ridden[key])
# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""

value = "June 3"
if value in miles_ridden:
    print(miles_ridden["June 3"])
else:
    print("Entry not found")
# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
value2 = "June 6"
if value2 in miles_ridden:
    print(miles_ridden["June 6"])
else:
    print("Entry not found")

# Use the items method to print the miles_ridden dictionary
print(miles_ridden.items())

# Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())
# Use the pop method to remove june 4 then print the contents of the dictionary
miles_ridden.pop("June 4")
print("After popping June 4th:")
print(miles_ridden.items())
# Use the values method to print the contents of the miles_ridden dictionary
print(miles_ridden.values())

# TODO 9.2 Sets
# Create an empty set named my_set
my_set = set()
# Create a set named days that contains the days of the week
days = {'Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat'}
# ---Pycharm complained about using set(), so I did what it said to do using {}---
# get the number of elements from the days set and print it
print(len(days))
# Remove Saturday and Sunday from the days set
days.discard('Sunday')
days.discard('Saturday')
# Determine if 'Mon' is in the days set
if 'Mon' in days:
    print("Mon is in the set days")
else:
    print("Mon is not in the set days")
# TODO 9.3 Serializing Objects (Pickling)

# import the pickle library
# ---I put it at the top of file so pycharm doesn't complain---
# create the output file log and open it for binary writing
log = open('log.bin', 'wb')
# pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, log)
# close the log file
log.close()
