# EXERCICIO 03
# Ler a nota de N alunos, depois dar a media e o valor dos conceitos
# Testes automatizados.

# Neste exercício, considere a seguinte a regra para conversão de nota para conceito:
# >=9 e  <=10 : A
# >=8 e <9: B
# >=7 e <8: C
# >=5 e <7: D
# <5: F

from statistics import mean

studentsNumber = int(input())
studentValues = []
studentConceitos =  {
  "A": 0,
  "B": 0,
  "C": 0,
  "D": 0,
  "F": 0
}

for i in range(studentsNumber):
    thisStudent = int(input())
    studentValues.append(thisStudent)

for i in range(studentsNumber):
    if (studentValues[i] >=9):
        thisConceito = "A"
    elif(studentValues[i] >=8):
        thisConceito = "B"
    elif(studentValues[i] >=7):
        thisConceito = "C"
    elif(studentValues[i] >=5):
        thisConceito = "D"
    else:
        thisConceito = "F"

    studentConceitos[thisConceito] = studentConceitos[thisConceito] + 1


for j in studentConceitos:
    print(f"{j}: {studentConceitos[j]}")

studentMean = mean(studentValues)

print(f"Media: {studentMean:0.2f}")