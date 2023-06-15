# EXERCICIO 01
# Ler um numero N de valores, e retornar o valor maior
# Testes automatizados.

totalNum = int(input())
numList = []


for i in range(totalNum):
    numList.append(int(input()))

print(max(numList))