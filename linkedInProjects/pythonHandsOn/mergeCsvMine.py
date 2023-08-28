import csv

def listCleaner(inputList, outputList):
        for x in range(len(inputList)):
            if isinstance(inputList[x], list):
                listCleaner(inputList[x], outputList)
            else:
                if inputList[x] not in outputList:
                    outputList.append(inputList[x])

def merger(files, output="newFile.txt"):
    rows = []
    rawHeaders = []
    for item in range(len(files)):
        with open(files[item], "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            rawHeaders.append(next(reader))
            for row in reader:
                rows.append(row)
    
    headers = []
    listCleaner(rawHeaders, headers)
    
    with open(output, "w", encoding="utf-8") as newfile:
        writer = csv.writer(newfile)
        
        writer.writerow(headers)
        writer.writerows(rows)
        
    return 0

if __name__ == "__main__":
    merger(files=["class1.csv", "class2.csv"], output="class3.csv")