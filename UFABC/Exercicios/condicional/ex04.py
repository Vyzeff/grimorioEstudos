# EXERCICIO 04
# Obter o prazo de entrega de uma fabrica de disco voadores.
# Testes automatizados.

def obter_prazo_entrega(disco1, disco2, disco3):
    expectedDate = int()

    if(disco1 == disco2 == disco3):
        expectedDate = 5
    elif(disco1 == disco2 or disco2 == disco3 or disco3 == disco1):
        expectedDate = 15
    else:
        expectedDate = 30
    return expectedDate
    