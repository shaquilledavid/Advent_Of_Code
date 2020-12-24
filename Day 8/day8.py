""" Advent of Code Day 8
https://adventofcode.com/2020/day/8

You are interrupted by the kid sitting next to you. Their handheld game
console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code
(your puzzle input) of the device. You should be able to fix it, but first
you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of
text. Each instruction consists of an operation (acc, jmp, or nop) and an
argument (a signed number like +4 or -20).
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1
(acc +1) and jmp +4 sets the next instruction to the other acc +1 near the
bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting
the next instruction to the only acc +3. It sets the accumulator to 5, and
jmp -3 causes the program to continue back at the first acc +1.

EXAMPLE
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

This is an infinite loop: with this sequence of jumps, the program will run
forever. The moment the program tries to run any instruction a second time,
you know it will never terminate.

Immediately before the program would run an instruction a second time, the
value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed
a second time, what value is in the accumulator?

"""

# I think this shouldn't be too difficult. I know that I can get the instructions
# into a list. Each list element will have an instruction and a value. I'll have
# a while loop, an index variable, and a second list to track which indices have
# been visited already. We will iterate through the instructions, checking each
# time if the index has been visited already. If the index has, return the current acc

with open("instructions.txt") as f:
    instructions = f.readlines()

ins = [str(x.strip()) for x in instructions]

#separate instructions from values so we can access them easier
ins = [i.split() for i in ins]

def accumulatorBeforeLoop(instructions):
    accumulator = 0
    indices_visited = []
    i = 0

    while i < len(instructions):
        
        if i in indices_visited:
            return accumulator
        
        if i not in indices_visited:
            indices_visited.append(i)
            
        if instructions[i][0] == 'acc':
            accumulator = accumulator + int(instructions[i][1])
            i = i + 1

        else:
            if instructions[i][0] == 'jmp':
                i = i + int(instructions[i][1])
            elif instructions[i][0] == 'nop':
                i = i + 1

print("The answer to PART A of my puzzle is " + str(accumulatorBeforeLoop(ins)))

"""--- Part Two ---
Somewhere in the program, either a jmp is supposed to be a nop, or a nop is
supposed to be a jmp. (No acc instructions were harmed in the corruption of
this boot code.)

Fix the program so that it terminates normally by changing exactly one jmp
(to nop) or nop (to jmp). What is the value of the accumulator after the
program terminates?
"""

#We can approach this situation by changing each nop/jmp one at a time
#but i think this approach is the longest, most taxing approach (brute force)


#alter the accumulator function from part A so we can see the indices in a global variable
def accumulatorBeforeLoop2(instructions):
    accumulator = 0
    i = 0
    ind = []

    while i < len(instructions):
        
        if i in ind:
            return 'change did not work'
        
        if i not in ind:
            ind.append(i)
            
        if instructions[i][0] == 'acc':
            accumulator = accumulator + int(instructions[i][1])
            i = i + 1

        else:
            if instructions[i][0] == 'jmp':
                i = i + int(instructions[i][1])
            elif instructions[i][0] == 'nop':
                i = i + 1
                
    return accumulator



def changeNop(instructions):
    accu = []
    i = 0
    copy_instructions = instructions
    
    while i < len(instructions):
        if instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'
            if accumulatorBeforeLoop2(instructions) == 'change did not work':
                instructions[i][0] = 'nop' #change it back
                i = i + 1
            elif accumulatorBeforeLoop2(instructions) != 'change did not work':
                                        return accumulatorBeforeLoop2(instructions)
        i = i + 1
        
    return 'changing the nops are useless'
            
def changeJmp(instructions):
    accu = []
    i = 0
    copy_instructions = instructions
    
    while i < len(instructions):
        if instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop'
            if accumulatorBeforeLoop2(instructions) == 'change did not work':
                instructions[i][0] = 'jmp'
                i = i + 1
            elif accumulatorBeforeLoop2(instructions) != 'change did not work':
                                        return accumulatorBeforeLoop2(instructions)
        i = i + 1
        
    return 'changing the jmps are useless'    
    
if changeNop(ins) == 'changing the nops are useless':
    print("The answer to PART B of my puzzle is " + str(changeJmp(ins)) + ", by changing a single jmp instruction")

else:
    print("The answer to PART B of my puzzle is " + str(changeNop(ins)) + ", by changing a single nop instruction")
    
