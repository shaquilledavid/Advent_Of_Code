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










