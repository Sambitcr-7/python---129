import random
ranNumber = random.randint(1,100)
print(ranNumber)
userGuess = None
guesses = 0



while(userGuess != ranNumber):
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if(userGuess==ranNumber):
        print("You guessed it right!")
    else:
        if(userGuess>ranNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")



print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(guesses)    