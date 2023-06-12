# EXERCICIO 02
# Ler vetor de tamanho N, entao seus N elementos e dizer se eh um vetor de dupla
# Testes automatizados.

# AINDA NÃO FINALIZADO

vectorSize = int(input())
vector = []

for i in range(vectorSize):
    vector.append(int(input()))


isFirst = True
isDouble = True
for j in vector:
    if isFirst:
        if vector[j] == vector[j+1]:
            isFirst = False
        else:
            isDouble = False
            break
    else:
        isFirst = True
        continue
        
if isDouble:
    print("Eh um vetor de duplas!")
else:
    print("Nao eh um vetor de duplas!")