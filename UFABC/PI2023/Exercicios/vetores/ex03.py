# EXERCICIO 03
# Uma função simples que intercala valores de v1 e v2 em um unico vetor v3
# Testes automatizados.
# Nao eh permitido utilizar as funcoes de listas: del, append, extend, insert, remove, pop.


def intercalar(v1, v2):
    v3 = {}

    for i in range(len(v1)):
        nowLen = len(v3)
        v3[nowLen] = v1[i]
        v3[nowLen + 1] = v2[i]

    why = list(v3.values())
    return why
