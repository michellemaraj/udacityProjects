"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

callSet = set()
longestTime = 0
phone = ""

for x in calls:
    callSet.add(x[0])
    callSet.add(x[1])

'''
function: returnCallsWithTotal
purpose: return the total time the phone number was on the phone
         in a list
'''
def returnCallsWithTotal(callSet, calls):
    newlist= []
    t=0
    for phone in callSet:
        for call in calls:
           if phone == call[0] or phone == call[1]:
               t += int(call[3])
        newlist.append([phone,t])
    return newlist

'''
function: returnLongestTime
purpose: find the phone that spent the longest time on the phone and return that
'''
def returnLongestTime(resultList,longestTime, phone):
    for x,y in resultList:
        if y > longestTime:
            phone = x
            longestTime = y
        else:
            phone = x
            longestTime = longestTime
    return [phone, longestTime]

resultList = returnCallsWithTotal(callSet, calls)
phone, longestTime= returnLongestTime(resultList,longestTime, phone)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, longestTime))
