import random

#scores
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_pick == 'q':
        break

    if user_pick not in["rock", "paper", "scissors"]:
        continue
    else:
        random_number= random.randint(0,2)
        #rock = 0, paper =1, scissors = 2
        computer_pick = options[random_number]
        print("computer picked", computer_pick+".")

        if user_pick == "rock" and computer_pick == "scissors":
            print("You won")
            user_wins += 1
        elif user_pick == "paper" and computer_pick == "rock":
            print("You won")
            user_wins += 1
        elif user_pick == "scissors" and computer_pick == "paper":
            print("You won")
            user_wins += 1
        else:
            print("You lost")
            computer_wins+=1
    
print("you won", user_wins , "times.")
print("computer won", computer_wins , "times.")
print("Goodbye")