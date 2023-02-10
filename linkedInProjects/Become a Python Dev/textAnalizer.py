text = input("Gimme a text,  cmon \n")

dict = {}

for x in text.lower().split():
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

print(f"The number each word in your text is: {dict}")