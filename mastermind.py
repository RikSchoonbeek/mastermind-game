# ------ TO DO ------
# * user can still give faulty input by entering a float, this has to be taken care of @ GetInput
# Change input type from int to string for easier handling

from random import randint


# Determine numbers to be guessed
def determineNumbers():
    number = ''
    for i in range(4):
        number += str(randint(0,9))
        

# Get user input, make sure it is a 4 digit int and communicate with user
def getInput():
    message = ''
    intCheck = False
    digitCheck = False
    while intCheck is False or digitCheck is False:
        guess = input("Enter your guess here: ")
        if len(guess) != 4:
            print('You entered ' + str(len(guess)) + ' digits, please enter 4.')
            digitCheck = False
        else:
            digitCheck = True

        for i in guess:
            if i not in '0123456789':
                intCheck = False
            else:
                intCheck = True

        if intCheck is False:
                print('Your input can only exist of the numbers 0 to 9, no other characters are allowed.')
            
    return guess


# Check user input
def checkUserInput():
    guess = getInput()
    print(guess)

# Toon gegokte nummer en resultaten van vorige gok
def showOutput():
    pass


determineNumbers()
checkUserInput()
