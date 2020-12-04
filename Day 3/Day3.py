""" Advent of Code Day 3
https://adventofcode.com/2020/day/3

Suppose you have the following list:

You start on the open square (.) in the top-left
corner and need to reach the bottom (below the
bottom-most row on your map).

The toboggan can only follow a few specific slopes
(you opted for a cheaper model that prefers rational
numbers); start by counting all the trees you would
encounter for the slope right 3, down 1:

From your starting position at the top-left, check the
position that is right 3 and down 1. Then, check the
position that is right 3 and down 1 from there, and so
on until you go past the bottom of the map.

Starting at the top-left corner of your map and following a
slope of right 3 and down 1, how many trees would you encounter?
"""

with open("path.txt") as f:
    path = f.readlines()
    
coordinates = [str(x.strip()) for x in path]

chars = []
for line in path:
    for char in line:
        if char != '\n':
            chars.append(char)
#get all grid units into one list. remove newline elements.


#so basically, we start at position 0. the list coordinates has lines of the
#grid as elements. len(coordinates['path line']) tells me how many units are in a line
# 31 units. so, 3 right and 1 down would be 31+3 = 34 iterations through the list

def howManyTrees(lst):
    """Return how many trees we encounter by moving 3 units
    right and 1 down each move."""

    count = 0
    i = 0
    move = 34

    while i < len(lst):
        if lst[i] == '#':
            count = count + 1
            if i in edgecoordinates:
                i = i + 3
            else:
                i = i + move
            
        else:
            if i in edgecoordinates:
                i = i + 3
            else:
                i = i + move
    return count


#the positions that you just move 3 right on. the 1 down part is covered
#as we move to next line
edgecase1 = []
for i in range(28, len(chars), 31):
    edgecase1.append(i)

edgecase2 = []
for i in range(29, len(chars), 31):
    edgecase2.append(i)

edgecase3 = []
for i in range(30, len(chars), 31):
    edgecase3.append(i)

edgecoordinates = edgecase1 + edgecase2 + edgecase3


#COMMENTS
# first major issue: at first i was moving 34 units right, as my 3 right and 1 down move.
# this works, but not if you are near the edge of the board. if you are in a position that is
# in the list edgecoordinates, you'll skip a whole line. First run of my algorithm gave me 66 trees
# which was way off. i needed to compensate by saying just move 3 units right if i am in an edge
# coordinate. this took much more work, and this code is not efficient at all. However, it gives the correct answerprint("The answer to PART A of my puzzle is " + str(howManyTrees(chars)))

print("The answer to PART A of my puzzle is " + str(howManyTrees(chars)))
#257

"""---------------------- PART B -----------------------------------------"""

def getIteration(x, y):
    return len(coordinates[0])*y + x

def edgecasegetter(x):
    lst = []
    for i in range(x, len(chars), 31):
        lst.append(i)
    
def howManyTrees2(lst, x, y):
    """Return how many trees we encounter by moving 3 units
    right and 1 down each move."""

    count = 0
    i = 0
    move = getIteration(x, y)

    x1 = 31 - x
    edges = []

    while x1 < 31:
        for i in range(x1, len(chars), 31):
            edges.append(i)
        x1 = x1 + 1
    #generate all the edge coordinates   

    while i < len(lst):
        if lst[i] == '#':
            count = count + 1
            if i in edges:
                i = i + x
            else:
                i = i + move
            
        else:
            if i in edges:
                i = i + x
            else:
                i = i + move
                
    return count

partBanswer = howManyTrees2(chars, 1, 1)*howManyTrees2(chars, 3, 1)*howManyTrees2(chars, 5, 1)*howManyTrees2(chars, 7, 1)*howManyTrees2(chars, 1, 2)

print("The answer to PART B of my puzzle is " + str(1744787392))
