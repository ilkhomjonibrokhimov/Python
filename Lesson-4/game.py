import random 

while True:
    key = (random.randint(1, 100))
    count = 0
    while count < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > key:
            print("Too high!")
            count += 1
            
        elif guess < key:
            print("Too low!")
            count += 1
            
        else: 
            print("You guessed it right!")
            a = input("Do you want to play again? ")
            if a not in ["Y", "y", "YES", "yes", "ok"]:
                break

        if count == 10:
            print("You lost.")
            a = input("Do you want to play again? ")
            if a not in ["Y", "y", "YES", "yes", "ok"]:
                break
    if a not in ["Y", "y", "YES", "yes", "ok"]:
        break