# EXERCICIO 02
# Checar se uma equação do segundo grau tem resultado
# Testes automatizados.

from math import sqrt

variableA = int(input())
variableB = int(input())
variableC = int(input())

delta = (variableB**2) -(4*variableA*variableC)

if (delta < 0):
    print("Sem solucao real!")
    print(f"Delta = {delta:0.2f}")
elif (delta == 0):
    x1 = -variableB / (2*variableA)
    print(f"x = {x1:0.2f}")
else:
    root = sqrt(delta)
    x1 = (-variableB + root)/ (2*variableA)
    x2 = (-variableB - root)/ (2*variableA)
    if ( x1 > x2):                
        print(f"x1 = {x2:0.2f}")
        print(f"x2 = {x1:0.2f}")
    else:
        print(f"x1 = {x1:0.2f}")
        print(f"x2 = {x2:0.2f}")

