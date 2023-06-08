# EXERCICIO 04
# Ler uma sequencia de numeros indefinidos, parando quando o input for 0, e entao dar a soma aritmetica desses numeros.
# Testes automatizados.


isZero = False
totalNumbers = []
while(not isZero):
    thisInput = int(input())

    if (thisInput == 0):
        isZero = True
        totalSum = 0
        for i in totalNumbers:
            totalSum += i

        totalMean = totalSum / (len(totalNumbers))
        print(f"{totalMean:0.2f}")
    else:
        totalNumbers.append(thisInput)

