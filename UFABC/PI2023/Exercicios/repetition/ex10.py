# EXERCICIO 10
# Ler um numero N, printar uma piramide com essa altura
# Testes automatizados.

pyramidHeight = int(input())
startDigits = 1
printDigits = 1
totalDigits = (pyramidHeight*2)-1

while(startDigits <= pyramidHeight):
    for j in range(int((pyramidHeight-startDigits))):
        print("-", end="")
    for p in range(printDigits):
        print('1', end="")
    for j in range(int((pyramidHeight-startDigits))):
        print("-", end="")
    print("")
    startDigits += 1
    printDigits +=2
