# EXERCICIO 06
# Ler o valor de N, então realizar f(N)
# Testes automatizados.


nValue = int(input())
"""
    𝑓(𝑛)=∑𝑛𝑖=1∑8𝑗=1(𝑖+1).𝑗
"""

finalValue = int()

for i in range(nValue):
    for j in range(8):
        finalValue += ((i+1) +1)*(j+1)

print(finalValue)