'''quiz game where players will get a bunch of questions 
and they will get a score of 1 for each correct answer. 
Will display the total score at the end of the game'''

import random

print("Welcome to the math quiz!")

play = input("Do you want to play (y/n)?")
print (play)

if play != "y":
    quit()

print("Okay! Lets start the game!")

score = 0
for i in range(10):
    
    # 1 - addition, 2-subtraction, 3- multiplication, 4-division
    operator = random.randint(1,4)
    first = random.randint(1,10)
    second = random.randint(1,10)

    match(operator):
        case 1:
            print (first, "+", second)
            res = first + second
        case 2:
            print (first, "-", second)
            res = first - second
        case 3:
            print (first, "*", second)
            res = first * second
        case 4:
            print (first, "/", second)
            res = first / second
        case _:
            print("invalid!")

    user_res = float(input("answer is : "))
    if float(res) == user_res:
        score +=1 

print ("your final score is: ",score)


