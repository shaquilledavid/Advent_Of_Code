""" Advent of Code Day 6
https://adventofcode.com/2020/day/6

As your flight approaches the regional airport where you'll switch to a much
larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you
need to do is identify the questions for which anyone in your group answers
"yes".

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?
"""

with open("answers.txt") as f:
    a = f.readlines()

answers = [str(x.strip()) for x in a]
#--- taken from my day 4 code file. want to group the answers of a group together
p = []
i = 0
j = i

#group the answers together in a list
while i < len(answers):
    if answers[i] == '':  #if we encounter a newline, we know that what came before consists of a whole passport.
        #answers.remove(answers[i])
        p.append([answers[field] for field in range(j, i)]) #append to our new list the passport fields from left to right hence (range(j, i)) 
        j = i
        i = i + 1 #update the indexes.
    i = i + 1

#Ran into a bug where I was not able to pick up the last group's answer sheet
#This is because of my implementation of grouping the answers together. It only
#detects for a newline -> (if answers[i] == '')
#can certainly do a case for end of list and nearest '', but instead I shortcut and added a newline to end of the file.



#So now, in list p, i have the answers from each group separated as lists, in a big list
#say we're dealing with case 1: ['necytxmlfhsu', 'uecosjvlhpmk']

def uniqueYes(lst):
    """ Count the number of unique yes answers of a group. """
    yesQuestions = []
    count = 0
    i = 0
    while i < len(lst):
        for letter in lst[i]:
            if (letter not in yesQuestions) and (letter != ''):    #in case we run into some cases where the '' is picked up
                yesQuestions.append(letter)
                count = count + 1
            else: #if the question has already been answered yes to, this is not a unique answer
                pass
        i = i + 1
    return count
                
        
#gather the sum of each count
sumOfCounts = 0
for group in p:
    sumOfCounts = sumOfCounts + uniqueYes(group)

print("The answer to PART A of my puzzle is " + str(sumOfCounts))


"""--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread
one word in the instructions:

You don't need to identify the questions to which anyone answered "yes";
you need to identify the questions to which everyone answered "yes"!

For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?"""

#['necytxmlfhsu', 'uecosjvlhpmk']

def allYesQuestions(lst):
    yesQuestions = []
    i = 0
    while i < len(lst):
        for question in lst[i]:
            if yesQuestionHelper(question, lst) == 1 and (question not in yesQuestions):
                yesQuestions.append(question)
            else:
                pass
        i = i + 1
    return len(yesQuestions)

def yesQuestionHelper(letter, lst):
    """ Return 1 if letter is in EVERY element of the list"""
    i = 0
    while i < len(lst):
        if letter in lst[i]:
            i = i + 1
        else:
            return 0
    return 1

#clean up p list -> remove all ''. This would hinder our method
for group in p:
	for answer in group:
		if answer == '':
			group.remove(answer)


sumOfCounts2 = 0
for group in p:
    sumOfCounts2 = sumOfCounts2 + allYesQuestions(group)

print("The answer to PART B of my puzzle is " + str(sumOfCounts2))


