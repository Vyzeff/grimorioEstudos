# EXERCICIO 01
# Receber uma matriz de N linhas e N colunas, buscar um elemento nela
# Testes automatizados.


thisLines = int(input())
thisColums = int(input())

thisMatrix = [[0 for x in range(thisColums)] for y in range(thisLines)] 
print(thisMatrix)
for i in range(thisColums):
    for j in range(thisLines):
        nowInput = int(input())
        thisMatrix[i][j] = nowInput

print(thisMatrix)