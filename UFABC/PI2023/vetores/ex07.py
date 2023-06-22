# EXERCICIO 07
# Receber N numeros, e verificar se a lista resultante é espelhada. se N/2==N/2
# Testes automatizados.
from math import floor

thisSize = int(input())
thisList = []

for i in range(thisSize):
    nowNum = int(input())
    thisList.append(nowNum)

thisLen = len(thisList)


beforeHalf = []
thisHalfed = floor(thisLen/2)
for i in range(0,thisHalfed):
    beforeHalf.append(thisList[i])

laterHalf = []
for j in range(thisHalfed+1, thisLen):
    beforeHalf.append(thisList[i])

isSame = True
for x in range(thisLen):
    if beforeHalf[x] == laterHalf[thisHalfed-x]:
        continue
    else:
        isSame = False
        break

if isSame:
    print("SIM")
else:
    print("NAO")