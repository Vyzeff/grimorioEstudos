# EXERCICIO 05
# Receber N numeros, e verificar se um valor em um indece M é a soma de todos os outros valores.
# Testes automatizados.


thisSize = int(input())
thisList = []

for i in range(thisSize):
    nowNum = int(input())
    thisList.append(nowNum)


thisIndex = int(input())

thisPop = thisList.pop(thisIndex)

if thisPop != sum(thisList):
    print("Nao")
else:
    print("Sim")