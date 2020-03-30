"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
callSets = set()  # holds all  unique Bangalore calls

# find all Bangalore numbers and add to set or list
def getcalls(sets , value , lists):
    for x in lists:
        if re.match("\(.*\)", str(x[value])) or re.match("^[7|8|9].*\w ", str(x[value])):
           holdval = re.match("\(.*\)|(^.*\w )",str(x[1]))
           neval= holdval.group()
           sets.add(neval)

    return sets

# calls function getcalls to hold all  unique calling  Bangalore calls
convtList = list(getcalls(callSets , 0, calls))
convtList.sort()

# print results
print("The numbers called by people in Bangalore have codes:")
for y in convtList:
    print(y)

# # part b
"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

- Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# #get all calls from and to
count = 0
count2 = 0
for x in calls:
    count2 = count2 +1
    #
    if re.match("\(.*\)", str(x[1])) and re.match("\(.*\)", str(x[0])):
        #print(str(x[1]), str(x[0]))
        count = count + 1

calPercent = (count/count2) * 100
print(count, count2)

'''
Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
'''
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(calPercent))