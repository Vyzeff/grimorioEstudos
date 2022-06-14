def sortWords(file):
    wordDict = {"wordCount": 0}
    
    with open(file, "r", encoding="utf-8") as f:
        for row in f:
            rowTreated = row.upper().split()
            for word in rowTreated:
                try:
                    wordDict[word] += 1
                    
                except KeyError:
                    wordDict[word] = 1
                wordDict["wordCount"] += 1

    sortedDict = {key: val for key, val in sorted(wordDict.items(), key = lambda x: x[1])}
    
    print(sortedDict)
    print(f"The total word tally is: {wordDict['wordCount']}")
    return 1

# all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())

if __name__ == "__main__":
    userInput = input("Please give me a text file and I will count the unique words in it.\n")
    
    sortWords(userInput)