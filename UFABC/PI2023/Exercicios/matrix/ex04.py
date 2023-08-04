# EXERCICIO 04
# Receber uma matriz de N linhas e N colunas, somar os items pares.
# Testes automatizados.

thisSize = int(input())
thisMatrix = [[0 for c in range(thisSize)] for l in range(thisSize)]

for line in range(thisSize):
    thisItems = input().split(" ")
    for column in range(thisSize):
        thisMatrix[line][column] = int(thisItems[column])

nowPos = 0
nowSum = 0

for i in range(thisSize):
    for belowNum in range((thisSize - 1 - nowPos)):
        nowNum = thisMatrix[nowPos][belowNum]
        if nowNum % 2 == 0:
            nowSum += nowNum
    nowPos += 1

print(nowSum)
