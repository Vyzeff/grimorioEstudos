# EXERCICIO 05
# Devolver uma faixa de temperatura baseado no input
# Testes automatizados.

tempvalue = int(input())

if (tempvalue >= 250):
    print("Muito Alta")
elif(tempvalue >= 200):
    print("Alta")
elif(tempvalue >= 30):
    print("Normal")
elif(tempvalue >= -20):
    print("Baixa")
else:
    print("Muito Baixa")
