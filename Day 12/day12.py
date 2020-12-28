""" Advent of Code Day 12
https://adventofcode.com/2020/day/12

Your ferry made decent progress toward the island, but the storm came in faster
than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather
than giving a route directly to safety, it produced extremely circuitous instructions.
When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. Figure out where the
navigation instructions lead. What is the Manhattan distance between that location and
the ship's starting position?
"""

with open("directions.txt") as f:
    directions = f.readlines()
    
dirs = [str(x.strip()) for x in directions]
compass = ['n', 'e', 's', 'w']*1000

class Ship:

    def __init__(self, n, s, e, w, current_dir):
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.dir = current_dir
        
        self.position = 441 #start east

    def updatePosition(self, direction, units):
        
        if direction == 'N':
            self.n = self.n + units

        if direction == 'E':
            self.e = self.e + units

        if direction == 'S':
            self.s = self.s + units

        if direction == 'W':
            self.w = self.w + units

        if direction == 'F':
            if self.dir == 'e':
                self.updatePosition('E', units)
            if self.dir == 'n':
                self.updatePosition('N', units)
            if self.dir == 's':
                self.updatePosition('S', units)
            if self.dir == 'w':
                self.updatePosition('W', units)

        if direction == 'L':
            if units == 90:
                self.dir = compass[self.position - 1]
                self.position -= 1
            if units == 180:
                self.dir = compass[self.position - 2]
                self.position -= 2
            if units == 270:
                self.dir = compass[self.position - 3]
                self.position -= 3

        if direction == 'R':
            if units == 90:
                self.dir = compass[self.position + 1]
                self.position += 1 
            if units == 180:
                self.dir = compass[self.position + 2]
                self.position += 2
            if units == 270:
                self.dir = compass[self.position + 3]
                self.position += 3


myShip = Ship(0, 0, 0, 0, 'e')
i = 0
while i < len(dirs):
    myShip.updatePosition(dirs[i][0], int(dirs[i][1:]))
    i = i + 1

def manhattanDistance(Ship):
    """Sum of the absolute values of its east/west position
    and its north/south position"""

    return abs(Ship.n - Ship.s) + abs(Ship.e - Ship.w)

print("The answer to PART A of my puzzle is " + str(manhattanDistance(myShip)))

