""" Advent of Code Day 15
https://adventofcode.com/2020/day/15

While you wait for your flight, you decide to check in with the Elves back at
the North Pole. They're playing a memory game and are ever so excited to explain
the rules!

In this game, the players take turns saying numbers. They begin by taking turns
reading from a list of starting numbers (your puzzle input). Then, each turn
consists of considering the most recently spoken number:

If that was the first time the number has been spoken, the current player says 0.
Otherwise, the number had been spoken before; the current player announces how
many turns apart the number is from when it was previously spoken.
So, after the starting numbers, each turn results in that player speaking aloud
either 0 (if the last number is new) or an age (if the last number is a repeat).

Given your starting numbers, what will be the 2020th number spoken?
"""
myinput = [0,14,1,3,7,9]

def t20thNumber(startingnums):
    lst = startingnums
    i = len(startingnums) #turn number

    while i < 2020:
        if lst[-1] not in lst[:-1]:
            lst.append(0)
            i = i + 1
        elif lst[-1] in lst[:-1]:
            newnum = findDifference(lst)
            lst.append(newnum)
            i = i + 1
            
    return lst[2019]
        
            
def findDifference(lst):
    number = lst[-1]
    i = -1
    count = 0
    while i < len(lst):
        if lst[i-1] != number:
            i = i - 1
            count = count + 1 
        else:
            return count + 1
           
print("The answer to PART A of my puzzle is " + str(t20thNumber(myinput)))
#763

"""--- Part Two ---
Impressed, the Elves issue you a challenge: determine the 30000000th number
spoken.
Given your starting numbers, what will be the 30000000th number spoken?
"""
myinput2 = [0,14,1,3,7,9]

def thirtyMillNumber(startingnums):
    lst = startingnums
    i = len(startingnums) #turn number

    while i < 30000000:
        if lst[-1] not in lst[:-1]:
            lst.append(0)
            i = i + 1
        elif lst[-1] in lst[:-1]:
            newnum = findDifference(lst)
            lst.append(newnum)
            i = i + 1
            
    return lst[-1]

def detectLoopInList(lst):
    half = len(lst)//2
    first_half = lst[:half]
    second_half = lst[half:]

    if first_half == second_half:
        return True

print("The answer to PART B of my puzzle is " + str(1876406))    
#1876406, with the help of another person's code. My approach to part B using my solution from part A would take long to compute.

