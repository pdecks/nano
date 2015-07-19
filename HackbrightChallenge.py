import random

# function definition 
def guess_game():

    # define random number
    randNum = random.randrange(1,100)

    #set counter for guesses = 0
    guessCount = 0
    gameEval = False
    guessList = []
   
    while gameEval == False:
        # while guess != random number, ask user for a guess
        guess = int(input("Please enter a number between 1 and 100."))
        
        if guessCount > 0:
           # while unique = False, ask user for a new guess
           while guess in guessList:
               guess = int(input("Enter a unique guess between 1 and 100."))
    
        # store unique guess in guessList
        guessList.append(guess)
    
        # increment guess counter
        guessCount += 1
    
        # evaluate guess
        if guess > randNum:
            print("Your guess is too high. Try again!")
        if guess < randNum:
            print("Your guess is too low. Try again!")
        if guess == randNum:
           gameEval = True


    # end of game
    print("Correct! The number I was thinking of was",randNum,".")
    print("It took you",guessCount,"guesses.")

    return
   
guess_game()