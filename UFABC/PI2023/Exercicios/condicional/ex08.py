# EXERCICIO 08
# Verificar se pontos estão dentro de um retângulo
# Testes automatizados.

MAX_X = 22
MIN_X = -800
MAX_Y = 35
MIN_Y = -20

xValue = int(input())
yValue = int(input())


if (xValue > MAX_X or xValue < MIN_X):
    print("NAO")
elif (yValue > MAX_Y or yValue < MIN_Y):
    print("NAO")
else:
    print("SIM")