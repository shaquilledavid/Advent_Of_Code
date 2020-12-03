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

#NOTE. WORKING SOLUTION NEAR THE BOTTOM OF FILE.
#directly below was my first attempt in which I overcomplicated things.


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
                                
          
      
d = {'8-11 t': [' tttttttcttm', 'wdwd', 'ttttttttttttttttttttt', 'tttttttt', 't'],
     '8-12 t': [' ttttadawdawdcttm', 'tttttttt']}
totalTest = totalSuccessfulPasswords(d)


"""------------------------------------------------------------------------------------------------
------------------------------------WORKING SOLUTION--------------------------------------------"""


#So basically, I thought about it in the single case. Read the first line from the text doc
# 6-10 p: ctpppjmdpppppp
# 6 is my lower bound, 10 is upper, p is the letter, then the password. I need to separate these
# Use split and list concatenation to do this.

def isSuccessful(line):
    """ This function will return if the password is a successful password according to
        the protocol"""
    
    first_lst = line.split('-') #separate the lower bound -> ['6', '10 p: ctpppjmdpppppp']
    second_lst = [first_lst[0]] + first_lst[1].split(' ') # separate at the whitespaces -> ['6', '10', 'p:', 'ctpppjmdpppppp']

    return checker2(int(second_lst[0]), int(second_lst[1]), second_lst[2].strip(':'), second_lst[3])
    #call helper function. notice the third parameter calls strip again. this is to get rid of the colon
    

def checker2(lower, upper, letter, password):
    """This function will return a 1 if the password is successful
        or a 0 if it is not."""
    count = 0 # number of times the letter occurs
    
    for char in password:
        if char == letter:
            count = count + 1

    if (count >= lower) and (count <= upper):
        return 1 

    else:
        return 0

# lastly, check every line of the text file. I have already put every line into a list by doing passwords = [str(x.strip()) for x in passwords]

goodPasswords = 0
index = 0

while index < len(passwords):
	goodPasswords = goodPasswords + isSuccessful(passwords[index]) #total + result of this line
	index = index + 1


print("The answer to PART A of my puzzle is " + str(goodPasswords))
#493


""" PART TWO
Each policy actually describes two positions in the password, where 1 means the first character,
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept
of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences
of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?"""

def newPolicy(position1, position2, letter, password):
    count = 0
    i = 0

    if password[position1 - 1] == letter:
        count = count + 1

    if password[position2 - 1] == letter:
        count = count + 1

    if count == 1: #meaning that it is a valid password
        return 1
    
    else:
        return 0

    
def isSuccessful2(line):
    """ This function will return if the password is a successful password according to
        the NEW protocol"""
    
    first_lst = line.split('-')
    second_lst = [first_lst[0]] + first_lst[1].split(' ') 

    return newPolicy(int(second_lst[0]), int(second_lst[1]), second_lst[2].strip(':'), second_lst[3])

    
goodPasswords2 = 0
index2 = 0

while index2 < len(passwords):
	goodPasswords2 = goodPasswords2 + isSuccessful2(passwords[index2]) #total + result of this line
	index2 = index2 + 1

print("The answer to PART B of my puzzle is " + str(goodPasswords2))
#593
