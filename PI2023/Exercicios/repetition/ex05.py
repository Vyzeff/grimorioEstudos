# EXERCICIO 05
# Fazer um triango com N.
# Testes automatizados.


printSize = int(input())

for i in range(printSize):
    for j in range(i+1):
        print(i+1, end="")
    print("")