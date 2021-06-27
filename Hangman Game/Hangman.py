name = input("Enter you name : ")
print("Hello, welcome " + name + " to play Hangman")
print("So, what your first guess ?")
# here we set America
word = "vietnamese"

guesses = " "
# Your turn play
turn = 10
while turn > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print(i, end="")
        else:
            print("_", end="")
            failed +=1
    if failed == 0:
        print("\nYou won")
        break

    guess = input("\nGuess in character : ").lower()
    guesses += guess
    if guess not in word :
        turn -= 1
        print("Wrong guess")
        print("You have ", + turn , "more times")
        if turn == 0:
            print("You lose")

