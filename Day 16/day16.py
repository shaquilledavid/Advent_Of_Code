""" Advent of Code Day 16
https://adventofcode.com/2020/day/16

You collect the rules for ticket fields, the numbers on your ticket, and the
numbers on other nearby tickets for the same train service (via the airport
security cameras) together into a single document you can reference (your puzzle
input).

The rules for ticket fields specify a list of fields that exist somewhere on
the ticket and the valid ranges of values for each field. For example, a rule
like class: 1-3 or 5-7 means that one of the fields in every ticket is named
class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and
5 are both valid in this field, but 4 is not).

...
It doesn't matter which position corresponds to which field; you can identify invalid
nearby tickets by considering only whether tickets contain values that are not
valid for any field. In this example, the values on the first nearby ticket are
all valid for at least one field. This is not true of the other three nearby
tickets: the values 4, 55, and 12 are are not valid for any field. Adding
together all of the invalid values produces your ticket scanning error rate:
4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket
scanning error rate?
"""

#first, I will need to read the file and get the ranges of each field into a list of lists
with open("input.txt") as f:
    inp = f.readlines()

inp = [str(x.strip()) for x in inp]
for x in inp:
    if x == '':
        inp.remove(x)

ranges = []
for elem in inp:
    if elem == 'your ticket:':
        break
    else:
        temp = elem.split(': ')[1]
        ranges.append(temp.split(' or '))
        
lst = []
for linerange in ranges:
    for raange in linerange:
        lst.append(raange.split('-'))

#step 1 complete

start = inp.index('nearby tickets:')
nearby_tickets = inp[start+1:]

#step 2 complete

invalid_values = []
def evaluateTicket(ticket, lst):
    values = ticket.split(',')
    
    for i in values:
        j = 0
        while j < len(lst):
            if int(i) in range(int(lst[j][0]), int(lst[j][1]) + 1):
                break
            if int(i) not in range(int(lst[j][0]), int(lst[j][1]) + 1):
                j = j + 1
            if j == len(lst):
                invalid_values.append(int(i))

#step 3 complete, wrote function to evaluate all the invalid values in the ticket        
for ticket in nearby_tickets:
    evaluateTicket(ticket, lst)

print("The answer to PART A of my puzzle is " + str(sum(invalid_values)))
#
