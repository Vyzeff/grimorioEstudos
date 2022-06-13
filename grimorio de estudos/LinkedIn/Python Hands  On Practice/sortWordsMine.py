def sortWords(phrase):
    
    wordDict = {}
    wordList = phrase.split()
    wordTreated = phrase.lower().split()
    
    for x, y in zip(wordTreated, wordList):
        wordDict[x] = y

    sortedDict = {key: val for key, val in sorted(wordDict.items(), key = lambda x: x[0])}
    sortedList = []
    
    for key in sortedDict.keys():
        sortedList.append(sortedDict[key])
    return sortedList

    # OR
    # return ''.join(sorted(input.split(), key = str.casef))
if __name__ == "__main__":
    userInput = input("Please give me a phrase and I will sort it.\n")
    
    print(sortWords(userInput))