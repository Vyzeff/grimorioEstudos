# EXERCICIO 03
# Receber uma matriz de N linhas e N colunas, comparar elas.
# Testes automatizados.


def comparar_matrizes(matriz1, matriz2):
    from math import floor

    isDouble = True
    try:
        for x in matriz2:
            for y in matriz2:
                if floor(int(matriz2[x][y])) == floor(int(matriz1[x][y]) * 2):
                    continue
                else:
                    isDouble = False
                    break
    except:
        isDouble = False

    return isDouble
