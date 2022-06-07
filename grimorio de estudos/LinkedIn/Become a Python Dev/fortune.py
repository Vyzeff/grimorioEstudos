from random import randint

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
    