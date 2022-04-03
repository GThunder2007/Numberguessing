import random
correctNumber = random.randint(1, 10)
chances = 0

while chances < 5:
    print("Hint: The Correct Number is: ", correctNumber)
    enterNumber = int(input("Guess a number between 1 - 10: "))
    if (enterNumber == correctNumber):
        print("Congrats! You guessed the number correct! The Number was: ", correctNumber)
        break
    if (enterNumber != correctNumber):
        print("Wrong guess, The correct number was: ", correctNumber)
        chances += 1
    