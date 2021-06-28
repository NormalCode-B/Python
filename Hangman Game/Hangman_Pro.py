import sys
import random
name = input("What your name? : ")
l = input("Input the word to start the game (between words ',') : ")
def run():
    print(f"Hello, {name}, let's play Hangman")
    print("Starting guesses............")
    # defining the word
    bag_words = l.split(',')
    words = random.choice(bag_words)
    turns = 10
    guesses = ""
    while turns > 0:
        failed = 0
        for i in words :
            if i in guesses:
                print(i, end="")
            else:
                print("_", end="")
                failed +=1
        if failed == 0:
            print("\nYou win")
            choice = input("Would you like to play again? y / n \n")
            if choice == "y":
                run()
            elif choice == "n":
                sys.exit()
            else:
                print("Something went wrong, type y or n")

        guess = input("\nGuess in character : ")
        guesses += guess
        if guess not in words :
            turns -=1
            print("Wrong")
            print(f"You have {turns} ")
            if turns == 0:
                print(" You lose")
                choice = input("Would you like to play again? y / n \n")
                if choice == "y":
                    run()
                elif choice == "n":
                    sys.exit()
                else:
                    print("Something went wrong, type y or n")
run()

