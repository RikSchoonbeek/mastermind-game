# ------ TO DO ------
# * user can still give faulty input by entering a float, this has to be taken care of @ GetInput
# Remove uneccesary comments
# Remove unecessary print from compareInput
# Remove unecessary print from determineSerie
# Write short and good comments
# Check for PEP8

# Add welcome message with explaination

from random import randint

def welcomeMessage():
    print('''
Welcome! This is a game of mastermind where the computer generates a serie of 4 
random numbers ranging from 0 to 9. You have to guess what the serie is.

You will be asked to enter 4 numbers in a row, ranging from 0000 to 9999. After
you have entered you will see the following:
- first number: how many characters you have guessed correct, but not on the correct position
- second number: how many characters are both correct and on correct position
- the serie you entered

Enjoy!

- Created by Rik Schoonbeek - rik.schoonbeek@gmail.com -
''')


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
        print('')
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
                print('Your input can only exist of the numbers 0 to 9.')
            
    return guess


# Check user input
def compareInput():
    welcomeMessage()
    number = determineSerie()
    playGame = True
    round = 1
    while playGame == True:
        correctChar = 0
        correctPos = 0
        guess = checkInput()
        # counting correct characters (not correct position)
        for char in guess:
            if char in number:
                correctChar += 1
        # counting correct character positions
        for i in range(len(number)):
            if guess[i] == number[i]:
                correctPos += 1

        print('Correct: {} | Correct and correct position: {} | Your guess: {}'.format(correctChar, correctPos, guess))

        if correctPos is 4:
            print('You guessed correct in {} rounds!'.format(round))
            print('Enter Y if you want to play again, anything else to quit.')
            playAgain = input('Play again: ').lower()
            if playAgain == 'y':
                playGame = True
                number = determineSerie()
                round = 1
            else:
                break

        round += 1


compareInput()
