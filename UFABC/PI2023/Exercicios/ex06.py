# EXERCICIO 06
# Calcular a soma dos termos de uma Progressão Aritmetica até N termos
# Testes automatizados.


initPos = int(input())
razaoPa = int(input())
totalNumbers = int(input())

finalPos = initPos + (totalNumbers - 1)*razaoPa
finalSum = (totalNumbers*(initPos + finalPos))/2

print(finalSum)