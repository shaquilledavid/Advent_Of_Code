""" Advent of Code Day 13
https://adventofcode.com/2020/day/13

Your notes (your puzzle input) consist of two lines. The first line is your
estimate of the earliest timestamp you could depart on a bus. The second line
lists the bus IDs that are in service according to the shuttle company; entries
that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you
can take to the airport. (There will be exactly one such bus.)

For example, suppose you have the following notes:

939
7,13,x,x,59,x,31,19
Here, the earliest timestamp you could depart is 939, and the bus IDs in service
are 7, 13, 59, 31, and 19.

The earliest bus you could take is bus ID 59. It doesn't depart until timestamp
944, so you would need to wait 944 - 939 = 5 minutes before it departs. Multiply
ing the bus ID by the number of minutes you'd need to wait gives 295.

What is the ID of the earliest bus you can take to the airport multiplied by the
number of minutes you'll need to wait for that bus?
"""

with open("times.txt") as f:
    times = f.readlines()

times = [str(x.strip()) for x in times]

times[1] = times[1].split(',')

l = []
for i in times[1]:
    if i != 'x':
        l.append(i)

times[1] = l
times[0] = int(times[0])
i = 0
while i < len(times[1]):
    times[1][i] = int(times[1][i])
    i = i + 1

# times = [1001798, [19, 41, 859, 23, 13, 17, 29, 373, 37]]
# times[0] is our earliest time, times[1] are all the bus id's in service
# buses run in increments in relation to its id. so bus 19 starts at 0, another at 19, 38... and so on
# we only want buses near our start time, so we can generate bus times starting at our start times.


def generateDepartures(bus_id, start_time):
    """Generate the next few departures of a bus AFTER the given starting time."""
    deps = []
    
    for i in range(0, start_time + 3*bus_id, bus_id):
        if i >= start_time:
            deps.append(i)

    return deps


def solver(lst):
    """Return the product of the earliest bus ID and the amount of time spent waiting.
       An input must be in the form of [START TIME, [BUS ID 1, BUS ID 2, ...]] 
    """
    departures = [generateDepartures(x, lst[0]) for x in lst[1]]
    x = min(departures)
    index_of_min = departures.index(x)

    optimal_bus_id = lst[1][index_of_min]
    minutes_waiting = x[0] - lst[0]
    
    return minutes_waiting*optimal_bus_id


print("The answer to PART A of my puzzle is " + str(solver(times)))
#203
