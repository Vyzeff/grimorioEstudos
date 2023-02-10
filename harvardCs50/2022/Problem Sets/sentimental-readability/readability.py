from cs50 import get_string

# Gets input from user
inputText = get_string("Please, input your text here: ")
# Length from input
textLength = len(inputText)
letters = 0
words = 1
sentences = 0

# Iterate for how many characters are there in inputText
for x in range(textLength):
    # Convert to lowercase
    text = inputText.lower()
    # Select a character from text, then gets its ASCII value
    char = ord(text[x])
    # If char is a lowercase letter
    if char >= 97 and char <= 122:
        letters += 1
    # If char is a space, add words
    elif char == 32:
        words += 1
    # If char is a . or ! or ?, add sentences
    elif char == 46 or char == 33 or char == 63:
        sentences += 1

# print(f"letters: {letters}")
# print(f"words: {words}")
# print(f"sentences: {sentences}")

# Coleman-Liau index
L = (letters / words) * 100
S = (sentences / words) * 100
calculation = 0.0588 * L - 0.296 * S - 15.8
grade = round(calculation)

# Print grade
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")