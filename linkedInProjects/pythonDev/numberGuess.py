from random import randint

target = randint(1, 125)
print("WELCOME!\n Today you are going to guess a number. Go on.")
iteration = 1
while True:
    try:
        guess = int(input(f"Your turn, this is your {iteration} try.\n"))
        if guess == target:
            print(f"CONGRATULATIONS!\n The number was {target}. It only took you {iteration} tries.")
            break
        elif guess < target:
            print("Higher.")
            iteration += 1
        else:
            print("Lower.")
            iteration += 1       
    except ValueError:
        print("That is not a number my friend. It will still count though")
        iteration += 1
    
    

        