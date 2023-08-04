# EXERCICIO 10
# Receber N numeros, retirar numeros repetidos da lista
# Testes automatizados.

thisSize = int(input())
thisList = []
thisInput = input().split(" ")

for i in range(thisSize):
    thisList.append(int(thisInput[i]))

thisTrueList = []
for x in range(thisSize):
    thisTrueList.append(thisList[x])
    countResult = thisTrueList.count(thisList[x])
    if countResult > 1:
        thisTrueList.pop()
    else:
        continue

for j in thisTrueList:
    print(j)
