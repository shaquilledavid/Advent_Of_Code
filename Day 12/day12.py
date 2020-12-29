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



# For this puzzle, instead of doing it the way I normally do (with list comprehension and using functions),
# I decided to work with Classes and Objects.

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

""" --- Part Two ---
Before you can give the destination to the captain, you realize that the actual
action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to
the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise)
the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given
number of degrees.
Action F means to move forward to the waypoint a number of times equal to the
given value.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""

class Ship2:

    def __init__(self, n, s, e, w, current_dir, way_x, way_y, dir1, dir2):
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.dir = current_dir
        self.way_x = way_x
        self.way_y = way_y
        self.dir1 = dir1
        self.dir2 = dir2
        
        self.position = 441 #start east
        self.position2 = 440 #start north

    def updatePosition(self, direction, units):
        
        if direction == 'N':
            self.way_y = self.way_y + units

        if direction == 'E':
            self.way_x = self.way_x + units

        if direction == 'S':
            self.way_y = self.way_y - units

        if direction == 'W':
            self.way_x = self.way_x - units

        if direction == 'F':
            if self.dir1 == 'n' and self.dir2 == 'e':
                self.n = self.n + self.way_y*units
                self.e = self.e + self.way_x*units
                
            if self.dir1 == 'n' and self.dir2 == 'w':
                self.n = self.n + self.way_y*units
                self.w = self.w + self.way_x*units

            if self.dir1 == 's' and self.dir2 == 'e':
                self.s = self.s + self.way_y*units
                self.e = self.e + self.way_x*units
                
            if self.dir1 == 's' and self.dir2 == 'w':
                self.s = self.s + self.way_y*units
                self.w = self.w + self.way_x*units

            if self.dir1 == 'e' and self.dir2 == 'n':
                self.e = self.e + self.way_x*units
                self.n = self.n + self.way_y*units
                
            if self.dir1 == 'e' and self.dir2 == 's':
                self.e = self.e + self.way_x*units 
                self.s = self.s + self.way_y*units

            if self.dir1 == 'w' and self.dir2 == 'n':
                self.w = self.w + self.way_x*units
                self.n = self.n + self.way_y*units

            if self.dir1 == 'w' and self.dir2 == 's':
                self.w = self.w + self.way_x*units
                self.s = self.s + self.way_y*units
            

        if direction == 'L':
            if units == 90:
                self.dir1 = compass[self.position - 1]
                self.position -= 1
                self.dir2 = compass[self.position2 - 1]
                self.position2 -= 1
                                    
            if units == 180:
                self.dir1 = compass[self.position - 2]
                self.position -= 2
                self.dir2 = compass[self.position2 - 2]
                self.position2 -= 2
                
            if units == 270:
                self.dir1 = compass[self.position - 3]
                self.position -= 3
                self.dir2 = compass[self.position2 - 3]
                self.position2 -= 3

        if direction == 'R':
            if units == 90:
                self.dir1 = compass[self.position + 1]
                self.position += 1
                self.dir2 = compass[self.position2 + 1]
                self.position2 += 1
                                    
            if units == 180:
                self.dir1 = compass[self.position + 2]
                self.position += 2
                self.dir2 = compass[self.position2 + 2]
                self.position2 += 2
                
            if units == 270:
                self.dir1 = compass[self.position + 3]
                self.position += 3
                self.dir2 = compass[self.position2 + 3]
                self.position2 += 3


m = Ship2(0, 0, 0, 0, 'e', 10, 1, 'e', 'n')

j = 0
while j < len(dirs):
    m.updatePosition(dirs[j][0], int(dirs[j][1:]))
    j = j + 1

#18391 too low
#30603 too low
#51249 true answer
print("The answer to PART A of my puzzle is 51249") #assisted by reddit thread
