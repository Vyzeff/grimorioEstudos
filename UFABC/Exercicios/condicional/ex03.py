# EXERCICIO 03
# Calcular o conceito final de um aluno.
# Testes automatizados.

test01 = float(input())
test02 = float(input())
test03 = float(input())

prova01 = float(input())
prova02 = float(input())

finalValue = ((test01 + test02 + test03)/3)*0.2 + 0.4*prova01 + 0.4*prova02

print(f"{finalValue:0.2f}")

""" 
Cálculo do Conceito Final (𝐶𝐹):
9.0≤𝑁𝐹≤10.0⟹𝐶𝐹=𝐴
7.5≤𝑁𝐹<9.0⟹𝐶𝐹=𝐵
6.0≤𝑁𝐹<7.5⟹𝐶𝐹=𝐶
5.0≤𝑁𝐹<6.0⟹𝐶𝐹=𝐷
𝑁𝐹<5.0⟹𝐶𝐹=𝐹
 """

if (finalValue >= 9):
    print("A")
elif(finalValue >= 7.5):
    print("B")
elif(finalValue >= 6):
    print("C")
elif(finalValue >= 5):
    print("D")
else:
    print("F")
