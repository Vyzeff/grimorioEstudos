# EXERCICIO 04
# Calcular a distância Manhatan entre dois pontos.
# Testes automatizados.

def calcular_distancia(x1, y1, x2, y2):
    manhatanValue = abs(x2 - x1) + abs(y2 - y1)
    return manhatanValue