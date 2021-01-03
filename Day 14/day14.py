""" Advent of Code Day 14
https://adventofcode.com/2020/day/14

After a brief inspection, you discover that the sea port's computer system uses
a strange bitmask system in its initialization program. Although you don't have
correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or
write a value to memory. Values and memory addresses are both 36-bit unsigned in
tegers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11
would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant
bit (representing 2^35) on the left and the least significant bit (2^0, that is,
the 1s bit) on the right. The current bitmask is applied to values immediately
before they are written to memory: a 0 or 1 overwrites the corresponding bit in
the value, while an X leaves the bit in the value unchanged.

To initialize your ferry's docking program, you need the sum of all values left
in memory after the initialization program completes. (The entire 36-bit address
space begins initialized to the value 0 at every address.)
"""

with open("input.txt") as f:
    inputs = f.readlines()

inp = [str(x.strip()) for x in inputs]

def changeToBinary(number):
    """Change a number to its 36 bit binary equivalent."""
    # https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
    return '{0:036b}'.format(number)

def maskNumber(mask, number):
    """Apply a mask to a number.

    >>> maskNumber('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11)
    000000000000000000000000000001001001
    """
    binary = changeToBinary(number)
    temp_lst = []
    #since python does not support string mutation, we will have to use a list
    i = 0
    j = 0
    while i < len(mask):
        if mask[i] == 'X':
            temp_lst.append(binary[i])
            i = i + 1
        else:
            temp_lst.append(mask[i])
            i = i + 1

    return ''.join([str(elem) for elem in temp_lst])
        
def binaryToNumber(binarynum):
    """Change a binary number to an integer base 2

    >>> binaryToNumber('000000000000000000000000000001100101')
    101
    """

    return int(binarynum, 2)

memory_addresses = {}

#these next few lines will be used to group memory instructions with masks
i = 0
ins = []
mems = []
while i < len(inp):
    if inp[i][:3] == 'mas':
        # i know the following stuff is a mem instruction
        ins.append(mems)
        ins.append(inp[i])
        mems = []
        i = i + 1
    else:
        mems.append(inp[i])
        i = i + 1
        
ins.append(mems) #last line
ins.remove([])

def applyMaskToDict(mask, value, address, dictionary):
    """Apply the mask operation to the value and insert it into the dictionary"""
    x = maskNumber(mask, value)
    dictionary[address] = binaryToNumber(x)

    return dictionary


### POPULATE THE DICTIONARY WITH THE MEMORY ADDRESSES AND VALUES AFTER MASKING.
# This code will be a little rough. It could be made better with simplification and variables.
# For example: ins[3][0].split(']')[0][4:] -> ins[3][0] gets the first memory instruction, splits it at the end ]. it returns this: ['mem[115', ' = 642']. We want just the 115 so we need to do [0][4:] 
index = 0
while index < len(ins):
    for mem in ins[index+1]:
        applyMaskToDict(ins[index][7:], int(mem.split('= ')[1]), mem.split(']')[0][4:], memory_addresses)
    index = index + 2

#now, the memory_addresses dictionary contains all the masked values applied to respective addresses. any overwriting will be automatically done as python's dictionary data structure takes care of that
print("The answer to PART A of my puzzle is " + str(sum(memory_addresses.values())))
#7611244640053

"""--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your
ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it
acts as a memory address decoder. Immediately before a value is written to memory,
each bit in the bitmask modifies the corresponding bit of the destination memory address
in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In
practice, this means the floating bits will take on all possible values, potentially
causing many memory addresses to be written all at once!

Execute the initialization program using an emulator for a version 2 decoder chip.
What is the sum of all values left in memory after it completes?
"""

def maskAddress(mask, addr):
    binary = changeToBinary(addr)
    temp_lst = []
    i = 0
    while i < len(mask):
        if mask[i] == '1':
            temp_lst.append(mask[i])
            i = i + 1
            
        elif mask[i] == 'X':
            temp_lst.append(mask[i])
            i = i + 1
        else:
            temp_lst.append(binary[i])
            i = i + 1
            
    return ''.join([str(elem) for elem in temp_lst])


#last semester, I learned about the ambiguous operator in Racket, -<, and sought a way to do so in python
#it turns out that using "yield from" is uses the same idea
#https://www.reddit.com/r/adventofcode/comments/kcr1ct/2020_day_14_solutions/gfsj0cd/?utm_source=reddit&utm_medium=web2x&context=3
#https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3
def generator(addr_mask):
    if 'X' in addr_mask:
        for r in ('0', '1'):
            yield from generator(addr_mask.replace('X', r, 1))
    else:
        yield addr_mask

part2dict = {}

def applyMaskedAddrToDict(mask, address, value, dictionary):
    """Apply the mask operation to the value and insert it into the dictionary"""
    x = maskAddress(mask, address)
    lst = []
    for i in generator(x):              #generate all the possbile addresses from the masking
        lst.append(binaryToNumber(i))   #didn't necessarily need to change to an int
        
    for addr in lst:                    #for each generated address, add it as a key with the intended value
        dictionary[addr] = value 

    return dictionary

index1 = 0
while index1 < len(ins):
    for mem in ins[index1+1]:
        applyMaskedAddrToDict(ins[index1][7:], int(mem.split(']')[0][4:]), int(mem.split(' = ')[1]), part2dict)
    index1 = index1 + 2

print("The answer to PART B of my puzzle is " + str(sum(part2dict.values())))
#3705162613854
