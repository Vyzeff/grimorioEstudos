# EXERCICIO 04
# 3 funções que irao, respectivamente, criar um vetor, imprimir e realizar um shift para a direita no vetor
# Testes automatizados.
# Nao eh permitido utilizar as funcoes de listas: del, append, extend, insert, remove, pop.


def inserir():
    why = {}
    for i in range(10):
        nowInput = int(input())
        why[i] = nowInput
    return list(why.values())


def imprimir(v):
    for i in v:
        print(f"{i} ", end="")
    print("")


def shift(v):
    thisLenght = len(v)
    lastItem = v[-1]
    firstItem = v[0]

    salt = thisLenght - 1
    while True:
        try:
            v[salt] = v[salt - 1]
            salt -= 1
        except:
            v[0] = lastItem
            break

    return v
