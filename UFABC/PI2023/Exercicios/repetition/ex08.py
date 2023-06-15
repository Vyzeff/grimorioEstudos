# EXERCICIO 08
# Calcular o valor de Π com base na serie de Gregory em N numeros
# Testes automatizados.


# AINDA NAO FINALIZADO

def calcular_pi(n):
    """
    Π/4=1/1−1/3+1/5−1/7+1/9...
    Π/n = 1/1 - 1/3... 1/n - 1/n+2 + 1/n + 3 -...
    """
    isSum = False
    nowNum = int()
    gregorValue = 1
    if n == 1:
        return 1
    for i in range(1,n+1):
        if (i)%2 == 0:
            nowNum = i+(i*2)
        else:
            nowNum = i
        if isSum:
            isSum = False
            gregorValue += 1/nowNum
        else:
            isSum = True
            gregorValue -= 1/nowNum
    return gregorValue