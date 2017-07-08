# ------ TO DO ------
# * user can still give faulty input by entering a float, this has to be taken care of @ GetInput
# Compare user input with generated serie
# Reprogram so that globals are not needed
# Remove uneccesary comments
# Add possibility to restart game after a win/lose

from random import randint


# Determine numbers to be guessed
def determineSerie():
    number = ''
    for i in range(4):
        number += str(randint(0,9))
    return number
        

# Get user input, make sure it is a 4 digit int and communicate with user
def checkInput():
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
def compareInput():
    number = determineSerie()
    # print(guess)
    print(number)
    notGuessed = True
    round = 1
    while True:
        correctChar = 0
        correctPos = 0
        guess = checkInput()
        # 1 Check how many chars are in both guess and number, but not in right position necessarily
        for char in guess:
            if char in number:
                correctChar += 1
        
        # 2 Check how many chars are in good position (if 4, then win).
        for i in range(len(number)):
            if guess[i] == number[i]:
                correctPos += 1

        print('{} {} {}'.format(correctChar, correctPos, guess))

        if correctPos is 4:
            print('You guessed correct in {} rounds!'.format(round))
            break

        round += 1


compareInput()
