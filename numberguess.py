import random

stop = int(input("Enter the number range \\"))
r = random.randint(0,stop+1)
print(r)
count = 0

while True:
    guess = int(input("guess the number"))

    if guess<0 or guess>stop:
        print("Enter a valid number in the given range")
        exit()
    
    if guess == r:
        print ( "You got it right in ",count+1, "chances")
        break
    else:
        count = count +1
    
        
    
