""" Advent of Code Day 2
https://adventofcode.com/2020/day/2

Suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number
of times a given letter must appear for the password to be
valid. For example, 1-3 a means that the password must contain
a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password,
cdefg, is not; it contains no instances of b, but needs at least 1.
The first and third passwords are valid: they contain one a or
nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

#Today is a bit trickier. First I would
#make them all strings and input these into a list
#Then I will convert the list to a dictionary
#finally I will loop over the dictionary checking
#which inputs satisfy its condition, and return the total

with open("passwords.txt") as f:
    passwords = f.readlines()
    
passwords = [str(x.strip()) for x in passwords]


def protocolAndPasswords(lst):
    """ Return a list of passwords and their related protocols"""
    
    retlst= []
    if lst == []:
        return retlst
    if len(lst) == 1:
        return retlst + (lst[0].split(':'))
    else:
        return protocolAndPasswords([lst[0]]) + protocolAndPasswords(lst[1:])

def convertToDict2(lst):
    """ Construct a dictionary with protocols as keys and passwords as values.
    Passwords are represented in lists to cover the case where there may
    be multiple passwords for a specific protocol.
    """
    
    d = {}
    i = 0
    while i < len(lst):
        if lst[i] in d:
            d[lst[i]].append(lst[i+1])
            i = i + 2
        else:
            entry = {lst[i]: [lst[i+1]]}
            d.update(entry)
            i = i+2
    return d


def inBounds(string, lower, upper, letter):
    """ This function will check if the number of occurences of the letter
    is in bounds with the protocol"""
    
    occ = 0
    for char in string:
        if char == letter:
            occ = occ + 1

    if (occ >= lower) and (occ <= upper):
        return 1
    else:
        return 0

def checker(protocol, passwords):
    """This function will count the number of passwords that adhere to
    the protocol"""
    
    count = 0
    #if i have something like '1-3 a'
    first_lst = protocol.split('-')
    second_lst = [first_lst[0]] + first_lst[1].split(' ')
    #separate all the meaningful things. we only want 1 3 and a
    i = 0

    if type(passwords) == type(None):
        return count
    
    for password in passwords:
        if (inBounds(password, int(second_lst[0]), int(second_lst[1]), second_lst[2])) == 1:
            count = count + 1
    return count

    #while i < len(passwords):
     #   check = inBounds(passwords[i], int(second_lst[0]), int(second_lst[1]), second_lst[2])
      #  count = count + check #check returns a 0 or 1 if the password follows protocol
       # i = i + 1
        
   # return count #count is the number of passwords that follow protocol
    
    
def totalSuccessfulPasswords(passworddict):
    total = 0
    for protocol in passworddict:
        total = total + checker(protocol, d.get(protocol))
    return total
                                
        
        
    
    
      
d = {'8-11 t': [' tttttttcttm', 'wdwd', 'ttttttttttttttttttttt', 'tttttttt', 't'], '8-12 t': [' ttttadawdawdcttm', 'tttttttt']}
totalTest = totalSuccessfulPasswords(d)

#if i run totalSuccessfulPasswords(convertToDict2(protocolAndPasswords(passwords))), i get an error saying cant check len of a NoneType
def count(dic): #this will count the values (passwords) that arent lists... but they are all lists
	c = 0
	for key in dic:
		if (type(dic.get(key))) != (type([])):
			c = c+1
	return c
