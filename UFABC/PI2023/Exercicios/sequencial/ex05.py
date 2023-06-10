# EXERCICIO 05
# Calcular a disntância entre dois pontos baseada em 4 inputs.
# Testes automatizados.

from math import sqrt

pointAx = int(input())
pointAy = int(input())
pointBx = int(input())
pointBy = int(input())


distance = sqrt((pointBx - pointAx)**2 + (pointBy - pointAy)**2)
print(f"{distance:.2f}")