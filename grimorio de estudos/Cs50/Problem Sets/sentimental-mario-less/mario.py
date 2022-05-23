from cs50 import get_int

# Always checks for h, if h is correct, break
while True:
    h = get_int("Please input the pyramid's desired height between 1 and 8: ")
    if h <= 8 and h >= 1:
        break

# Nested loop, for height then width
for x in range(h):
    for y in range(h):
        # Math mambo jumbo that does the logic for printing the pyramid
        if x + y >= h - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")

