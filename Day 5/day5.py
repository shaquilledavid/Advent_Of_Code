""" Advent of Code Day 5
https://adventofcode.com/2020/day/5

Instead of zones or groups, this airline uses binary space partitioning
to seat people. A seat might be specified like FBFBBFFRLR, where F means
"front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the
rows on the plane (numbered 0 through 127). Each letter tells you which half of
a region the given seat is in. Start with the whole list of rows; the first
letter indicates whether the seat is in the front (0 through 63) or the back
(64 through 127). The next letter indicates which half of that region the seat
is in, and so on until you're left with exactly one row.
"""
import math

with open("seats.txt") as f:
    seats = f.readlines()
    
allseats = [str(x.strip()) for x in seats]

#write the formula for calculating through the F and B's

def row(seat):
    """ Return the row number of a seat."""
    upper = 127
    lower = 0
    i = 0

    while i < len(seat):
        update = (upper - lower) / 2 
        if seat[i] == 'F':
            upper = math.floor(upper - update)
            i = i + 1
        elif seat[i] == 'B':
            lower = math.ceil(lower + update)
            i = i + 1
    if seat[-1] == 'F':
        return lower
    else:
        return upper

def column(seat):
    """ Return the column number of a seat."""
    upper = 7
    lower = 0
    i = 0

    while i < len(seat):
        update = (upper - lower) / 2 
        if seat[i] == 'L':
            upper = math.floor(upper - update)
            i = i + 1
        elif seat[i] == 'R':
            lower = math.ceil(lower + update)
            i = i + 1
    if seat[-1] == 'L':
        return lower
    else:
        return upper

def calculateID(row, column):
    return row*8 + column
    
allSeatIDs = []

for seats in allseats:
    allSeatIDs.append(calculateID(row(seats[:7]), column(seats[-3:])))

print("The answer to PART A of my puzzle is " + str(max(allSeatIDs)))
#894


""" --- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding
pass in your list. However, there's a catch: some of the seats at the very front
and back of the plane don't exist on this aircraft, so they'll be missing from
your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1
from yours will be in your list.

What is the ID of your seat?
"""

#so basically, if we sort our list of ids, our seat should be the ONLY one
#with a gap in the list
allSeatIDs.sort()
index = 0
lst = []

while index < len(allSeatIDs) - 1:
    if allSeatIDs[index] + 1 != allSeatIDs[index+1]:
        lst.append(allSeatIDs[index])
        index = index + 1
    index = index + 1

print("The answer to PART B of my puzzle is " + str(lst[0]+1)) #need to add 1 because lst[0] is the seat to the left of us
#579

	
    



