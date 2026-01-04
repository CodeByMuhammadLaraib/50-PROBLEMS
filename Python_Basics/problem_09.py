# problem_09.py
# number guessing game

import random as ran

def numChecker(numTaker):
    total_Count = 0
    while True:
        guessNum = int(input("Enter your number(1 to 100):"))

        if guessNum == numTaker and 1 <= guessNum <= 100:
            print(f"Your guess is correct {guessNum}. Your total guess is {total_Count}")
            break
        
        elif guessNum != numTaker and 1<= guessNum <= 100:

            if guessNum > numTaker:
                print("Too high")
                total_Count += 1

            elif guessNum < numTaker:
                print("Too low")
                total_Count +=1

            else:
                print("ERROR")
                numChecker(numTaker)
        else:
            print("Invalid input")
            numChecker(numTaker)


numGenerator = ran.randint(1, 100)

numChecker(numGenerator)