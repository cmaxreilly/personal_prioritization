import data
import helpers
import os
import sys

sorted_alphabetically = sorted(data.data)


# Test print

# print(helpers.creatArray(sorted_alphabetically))

# if the number of arguments is 1:
    # determine the number of each item in the list of worries
    # use this number to create a list of priorities in decending order
if len(sys.argv) == 1:
    print(data.data)

if len(sys.argv)== 2:
    if sys.argv[1] == "-d": # When script is called with -d:
        dat = open("data.py", "a") # open data.py in append mode as dat
        new_entry = str(input("what data would you like to input?\n")) # Ask "What data would you like to input?"
        dat.write("\ndata.append('{}')".format(new_entry)) # append code that writes data to list into dat
        dat.close() # close dat
 