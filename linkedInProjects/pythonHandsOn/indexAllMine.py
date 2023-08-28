def searchAll(searchList, search):
    indexList = list()
    ''' 
    for x, z in enumerate(searchList):
        if z == search:
            print([x])
            indexList.append([x])
        elif isinstance(z, list):
            for y in searchAll(searchList[z], search):
                indexList.append([x]+y)
     '''        
    for x in range(len(searchList)):
        if searchList[x] == search:
            indexList.append([x])
        elif isinstance(searchList[x], list):
            for y in searchAll(searchList[x], search):
                indexList.append([x]+y)
    return indexList     


if __name__ == "__main__":
    inputList = [1, 2, 3, 4, 5, 6, [1, 2, 3, 5, 6, [123, 2, 98]]]
    searchIndex = 2

    print(searchAll(inputList, searchIndex))