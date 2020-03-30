"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoingCalls = set()
receivingCalls = set()
textNumbers = set()

# x[0] == outgoing calls x[1] incoming calls

# get all unique outgoing calls and recieving calls
for x in calls:
    outgoingCalls.add(x[0])
    receivingCalls.add(x[1])

# get all unique text numbers
for y in texts:
    textNumbers.add(y[0])
    textNumbers.add(y[1])

'''The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.'''
outgoingDiffreceiving = outgoingCalls.difference(receivingCalls)
outgoingDiffRecivingAndText = outgoingDiffreceiving.difference(textNumbers)
sortedOrder = list(outgoingDiffRecivingAndText)
sortedOrder.sort()

print("These numbers could be telemarketers: ")
for num in sortedOrder:
    print(num)