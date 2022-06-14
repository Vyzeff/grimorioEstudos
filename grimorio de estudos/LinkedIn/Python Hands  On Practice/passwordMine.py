from random import randint
import re
def passwordGen(complex):
    with open("diceware.wordlist.asc", "r", encoding="utf-8") as f:
        password = []
        for x in range(int(complex)):
            diceNumber = []
            
            for y in range(5):
                diceNumber.append(randint(1,5))
            
            diceString = ""
            for z in range(5):
                diceString = diceString + str(diceNumber[z])
        
            for line in f:
                if diceString in line:
                    password.append("".join(re.findall(r"[0-9a-zA-Z-']+", line))[5:])
            f.seek(0)
    print("Your new password is")
    for item in password:
        print(item, end=" ")
    
    print("")
    return 0
if __name__ == "__main__":
    passComplex = input("Please input your desired password complexity, from 1 to 10: ")
    
    passwordGen(passComplex)
    