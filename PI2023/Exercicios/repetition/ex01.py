# EXERCICIO 01
# Calculo funçao 𝑓(𝑎,𝑏,𝑐)=𝑎+∑𝑏𝑑=1(𝑐.𝑑)
# Testes automatizados.

def obter_valor_funcao(a, b, c):
    finalValue = int()
    totalSum = 0
    for i in range(b):
        totalSum += (i+1)*c
    
    finalValue = a + totalSum

    return finalValue