import random

def dice(*dice):
    diceRolls = {}
    for y in range(1, 1000000):
        temp = 0
        for x in dice:        
            roll = random.randint(1, x)
            temp += roll
        try:     
            diceRolls[temp] += 1
        except:
            diceRolls[temp] = 1
            
    diceSorted = sorted(diceRolls.items())
    diceFinal = {key: val for key, val in diceSorted}
    for key, val in diceFinal.items():
        print(f"{key}: {(val/10000):0.2f}%")


if __name__ == "__main__":
    dice(4, 6, 6)