# EXERCICIO 06
# Receber N numeros, somar a soma de todos os vizinhos de qualquer numero 1
# Testes automatizados.


thisSize = int(input())
thisList = []

for i in range(thisSize):
    nowNum = int(input())
    thisList.append(nowNum)

thisSum = 0
while True:
    try:
        getIndex = thisList.index(1)
        numBefore = thisList.pop(getIndex-1)
        numAfter = thisList.pop(getIndex)

        thisList.pop(getIndex-1)
        thisSum += numBefore + numAfter
    except:
        print(thisSum)
        break
