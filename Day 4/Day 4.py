""" Advent of Code Day 4
https://adventofcode.com/2020/day/4

The automatic passport scanners are slow because
they're having trouble detecting which passports
have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Passport data is validated in batch files (your puzzle input).
Each passport is represented as a sequence of key:value pairs
separated by spaces or newlines. Passports are separated by blank lines.

Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields.Treat cid
as optional. In your batch file, how many passports are valid?
"""

#wanna write a function to read lines in the file
#put the elements in a list. if the line = \n, make new list

with open("passports.txt") as f:
    passports = f.readlines()

p = []
i = 0
j = i

#group the passports together in a list
while i < len(passports):
    if passports[i] == '\n':  #if we encounter a newline, we know that what came before consists of a whole passport.
        p.append([passports[field] for field in range(j, i)]) #append to our new list the passport fields from left to right hence (range(j, i)) 
        j = i
        i = i + 1 #update the indexes.
    i = i + 1

#remove the newlines
for passport in p:
    for field in passport:
        if field == '\n':
            passport.remove(field)
            
index = 0
index2 = 0
#I want all passports to be a list of length one. Currently some are a list of multiple elements, because of fields being on multiple lines from the file
while index < len(p):
    if len(p[index]) > 1:
        p[index] = ' '.join(p[index])
        index = index + 1
    else:
        p[index] = ' '.join(p[index])
        index = index + 1

def isValidPassport(passport):
    """Return 1 if the passport is valid, meaning it has all required fields.
       Otherwise return 0.
    """
    
    if ("byr" in passport) and ("iyr" in passport) and ("eyr" in passport) and ("hgt" in passport) and ("hcl" in passport) and ("ecl" in passport) and ("pid" in passport):
        return 1
    else:
        return 0

        
validpassports = 1
#generated number of valid passports
for passport in p:
    validpassports = validpassports + isValidPassport(passport)


print("The answer to PART A of my puzzle is " + str(validpassports))


"""------------------------------ PART B -----------------------------------------"""

"""The line is moving more quickly now, but you overhear airport security talking
about how passports with invalid data are getting through. Better add some data
validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about
what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and
valid according to the above rules.
"""

#we might as well go ahead and remove all invalid passports here.
p2 = []
for passport in p:
    if isValidPassport(passport) == 1:
        p2.append(passport)

#right now I have passports as list elements all in one line
#I need to split up keys and values into their own list
splitIndex = 0
newlist = []
while splitIndex < len(p2):
    split = p2[splitIndex].split()
    split2 = [field.split(':') for field in split]
    newlist.append(split2)
    splitIndex = splitIndex + 1
    

finallst = []
i = 0 #outer list
j = 0 #value index
while i < len(newlist):
    d = {}
    while j < len(newlist[i]):
        d[newlist[i][j][0]] = newlist[i][j][1]
        j = j + 1
    finallst.append(d)
    j = 0
    i = i + 1
          
#now in one large list, all passports are in their own dictionary with accessible values          
        
    
# Complete all the functions for validation checks 

def birthcheck(year):
    if int(year) <= 2002 and int(year) >= 1920:
        return True
    return False

def issuecheck(year):
    if int(year) <= 2020 and int(year) >= 2010:
        return True
    return False

def expirycheck(year):
    if int(year) <= 2030 and int(year) >= 2020:
        return True
    return False

def heightcheck(height):
    if height[-2:] == "cm":
        return int(str(height[0:-2])) >= 150 and int(str(height[0:-2])) <= 193
    if height[-2:] == "in":
        return int(str(height[0:-2])) >= 76 and int(str(height[0:-2])) <= 59
    else:
        return False

def haircheck(haircolor):
    if len(haircolor) == 7 and haircolor[0] == "#":
        return True
    return False

def eyecheck(color):
    if color == "amb" or color == "blu" or color == "brn" or color == "gry" or color == "grn" or color == "hzl" or color == "oth":
        return True
    return False

def idcheck(pid):
    if len(pid) == 9 and (isError(pid) == False):
        return True
    return False

def isError(pid):
    #return if changing the pid to an int will result in an error
    #implementation learned from https://stackoverflow.com/questions/34793339/true-if-a-function-works-and-false-if-a-function-gives-an-error
    try:
        int(pid)
        return False
    except Exception:
        return True

                
def isValidPassport2(p):
    """Return 1 if the passport is valid, meaning it has all required fields.
       Otherwise return 0.
    """

    if (birthcheck(p["byr"])) and (issuecheck(p["iyr"])) and (expirycheck(p["eyr"])) and (heightcheck(p["hgt"])) and (haircheck(p["hcl"])) and (eyecheck(p["ecl"])) and (idcheck(p["pid"])):
        return 1
    return 0
        
        
#return final number of valid passports with new restrictions
total = 0
i = 0
while i < len(finallst):
    total = total + isValidPassport2(finallst[i])
    i = i + 1
    
print("The answer to PART B of my puzzle is " + str(total))
#the correct answer is 111.
