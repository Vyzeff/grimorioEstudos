# EXERCICIO 08
# Receber N numeros, e verificar se o vetor é crescente
# Testes automatizados.

thisSize = int(input())
thisList = []
thisInput = input().split(" ")

for i in range(thisSize):
    thisList.append(thisInput[i])

thisLen = len(thisList)

isCrescent = True
for x in range(thisLen):
    try:
        if thisList[x] <= thisList[x + 1]:
            continue
        else:
            isCrescent = False
            break
    except:
        break

if isCrescent:
    print("SIM")
else:
    print("NAO")
