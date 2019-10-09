#exercise long 3: Guess a number

import random

attempts=5
play="y"

while(play.lower() == "y" ):
    win=False
    s_num=guess=random.randint(1,10)
    print("I am thinking of a number between 1 and 10.")
    for i in range(attempts):
        print(f'You have {attempts-i} guesses left')
        num=int(input("What is your guess? "))
        if(num>s_num):
            print("Too high")
        elif(num<s_num):
            print("Too low")
        else:
            win=True
            break
    if(win):
        print("Yes! You win!")
    else:
        print("Sorry you ran out of guesses!")

    play=input("Do you want to play again (Y or N)? ")

print("Bye")
