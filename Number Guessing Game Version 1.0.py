# Goal: The computer chooses a random number from 1–100. The user keeps guessing until they find it.

#Version 1.0

import random

while True:

    #Old code */
    ran_num=random.randint(1,100)
    count=0
    while True:
        guess=int(input("Enter your guess: "))  
        if guess!=ran_num:
            if guess>ran_num:
                print("Too high")
                count+=1
            elif guess<ran_num:
                print("Too Low")
                count+=1
        elif guess==ran_num:
            print("Correct!...")
            break
        else:
            print("Error...Plese Try another input.")

    print("Your Score is :",count)      #Printing the attempts/Score take to win
    #* /
    
    #Logic for restart the game
    print("Do you want to play again ?")
    print('1.Yes')
    print('2.No')
    choice=int(input("Enter your choice:"))

    if choice==1:
        continue 
    else:
        print("Have a nice day.")
        break