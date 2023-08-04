# EXERCICIO 02
# Receber uma matriz de N linhas e N colunas, tirar a media das notas dos alunos na matriz.
# Testes automatizados.


thisLines = int(input())
thisColumns = int(input())
thisMatrix = [[0 for c in range(thisColumns)] for l in range(thisLines)]
for linha in range(thisLines):
    thisItem = input().split(" ")
    for coluna in range(thisColumns):
        thisMatrix[linha][coluna] = float(thisItem[coluna])


for student in thisMatrix:
    nowSum = 0
    for grade in student:
        print(f"{grade:0.2f} ", end="")
        nowSum += grade

    finalResult = nowSum / len(student)
    # student.append(finalResult)
    print(f"{finalResult:0.2f}")
