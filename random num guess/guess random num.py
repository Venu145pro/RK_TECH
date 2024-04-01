import random
def guessing_game(lwrbound,uprbound,max_attempts):
    #generate random number between the given range
    secret_number=random.randint(lwrbound,uprbound)
    attempts=0
    while attempts<max_attempts:
        guessed_num=int(input(f"Guess the number between {lwrbound} and {uprbound}:  "))
        if guessed_num<secret_number:
            print("Try again! your guessed_num was too small.")
        elif guessed_num>secret_number:
            print("Try again! Your guessed_num was too high.")
        else:
            print("Congratulations! You guessed the number correctly")
            return
        attempts+=1
    print(f"Better luck next time!The number was {secret_number}.")
    #setting the range and maximum number of attempts
lwrbound=1        
uprbound=100       
max_attempts=5     
        #Start the game
guessing_game(lwrbound,uprbound,max_attempts)
