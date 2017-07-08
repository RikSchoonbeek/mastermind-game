# ------ TO DO ------
# * user can still give faulty input by entering a float, this has to be taken care of @ GetInput

from random import randint


# Determine numbers to be guessed
def DetermineNumbers():
    x = ''
    for i in range(4):
        x += str(randint(0,9))
        

# Get user input, make sure it is a 4 digit int and communicate with user
def GetInput():
    message = ''
    intCheck = False
    digitCheck = False
    while intCheck is False or digitCheck is False:
        try:
            guess = int(input("Enter your guess here: "))
            intCheck = True
        except ValueError:
            print('Your input can only exist of the numbers 0 to 9, no other characters are allowed.')
            intCheck = False

        if len(str(guess)) != 4:
            print('You entered ' + str(len(str(guess))) + ' digits, please enter four.')
            digitCheck = False
        else:
            digitCheck = True
            
    return guess


# Check user input
def CheckUserInput():
    guess = GetInput()
    print(guess)

# Toon gegokte nummer en resultaten van vorige gok
def ShowOutput():
    pass


DetermineNumbers()
CheckUserInput()
