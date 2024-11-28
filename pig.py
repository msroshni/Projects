# project from tech with tim
import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

while True:
    players = input("Enter the number of players (1-4)")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("must be between 1 and 4")
    else:
        print("Invalid,try again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores)<max_score:

    for idx in range(players):
        print("\nPlayer", idx+1 , "turn has started\n")
        print("\nYour total score is : ", player_scores[idx],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll the dice(Y) ?")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                current_score=0
                print("You rolled a 1!, turn done")
                break
            else:
                current_score+=value
                print("You rolled : ", value)
            print("Your score is ", current_score)

        player_scores[idx] += current_score
        print("Your total score is ", player_scores[idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nplayer",winning_idx+1,"is the winner with score", max_score,"\n")