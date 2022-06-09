from random import randint
#import re
#import string

fortuneSlips = {
    1: "A disaster is coming",
    2: "A dream you have will come true.",
    3: "A new voyage will fill your life with untold memories.",
    4: "A stranger, is a friend you have not spoken to yet.",
    5: "It is now, and in this world, that we must live.",
    6: "Wouldn’t it be ironic to die in the living room?",
    7: "run.",
    8: "No snowflake in an avalanche feels responsable.",
    9: "About time I got out of that cookie."
}

input = input("Want a cookie?").lower()
lucky = randint(1, 125)

if input == "y" or input == "yes":
    print(fortuneSlips[randint(1, 9)] + f" Plus your lucky number is {lucky}")
elif input == "n" or input == "no":
    print("Then what the hell are you doing in a fortune cookie app?")
else:
    print("...? Sorry?")
    
'''     def test(text):
            return any(x in string.punctuation for x in text) '''

'''         
def anualBirthsAverage(year, births):
    avr = 0
    for x, y in zip(year, births):
        if avr == 0:
            avr = births
        else:
            avr = round(avr + births // 2)
        print(f"In the year {x}, there were {y} births, and the running average was {avr}.") '''

'''         
def palindrome(word):
    cleanWord = re.sub("\W+", "", word).lower()
    if cleanWord is reversed(cleanWord):
        return True '''
    