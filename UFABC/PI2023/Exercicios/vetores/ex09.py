# EXERCICIO 08
# Receber N numeros em 2x em 2 vetores diferentes, e verificar se um deles eh multiplicado pela mesma fração em relação ao outro
# Testes automatizados.

thisSize = int(input())
thisList1 = []
thisList2 = []
thisInput = input().split(" ")

for i in range(thisSize):
    thisList1.append(int(thisInput[i]))

thisInput2 = input().split(" ")
for j in range(thisSize):
    thisList2.append(int(thisInput2[j]))

thisDivision = round(thisList1[0] / thisList2[0])
isMulti = True
for x in range(thisSize):
    if (round(thisList1[x] / thisList2[x])) != thisDivision:
        isMulti = False
        break
    else:
        continue

if isMulti:
    print("SIM")
else:
    print("NAO")
