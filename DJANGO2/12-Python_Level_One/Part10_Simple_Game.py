###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

import random

def pcGuess():
    digits = list(range(10))
    random.shuffle(digits)
    pc = digits[:3]
    rannum = ''.join(str(x) for x in pc)
    return rannum

rannumPC = pcGuess()
print(rannumPC)

def userPlay():
    guess = input("What is your guess? ")
    return guess

counter = 0
status = False
def countTry():
    global counter
    global status
    counter += 1
    if counter == 3:
        print("Here is a clue{a}".format(a=rannumPC[0]))
    elif counter == 6:
        print("Here is a clue{a}".format(a=rannumPC[1]))
    elif counter == 9:
        print("Game Over")
        status =  True


while not status:
    userGuess = userPlay()
    if userGuess == rannumPC:
        print("Correct!")
        status = True
        break

    elif rannumPC[0] in userGuess or rannumPC[1] in userGuess or rannumPC[2] in userGuess:
        print("You're almost there! Some are right, other are wrong")
        countTry()


    else:
        print("All the digits are wrong!")
        countTry()

#finish


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
