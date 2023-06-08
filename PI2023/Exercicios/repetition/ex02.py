# EXERCICIO 02
# Ler N numeros depois de N e dar a soma, media, minimo e máximo deles.
# Testes automatizados.

from statistics import mean

listSize = int(input())
allNumbers = []

for i in range(listSize):
    thisNumber = int(input())
    allNumbers.append(thisNumber)

listSum = sum(allNumbers)
listMean = mean(allNumbers)
listMin = min(allNumbers)
listMax = max(allNumbers)


print(listSum)
print(listMean)
print(listMin)
print(listMax)