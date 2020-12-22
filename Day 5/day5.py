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

