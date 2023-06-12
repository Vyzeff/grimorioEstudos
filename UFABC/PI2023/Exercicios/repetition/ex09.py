# EXERCICIO 09
# Ler um numero N, e retornar seus valores na ordem inversa.
# Testes automatizados.

normalNum = input()
normalNumLen = len(normalNum)
for i in range(normalNumLen):
    print(normalNum[normalNumLen-i-1])
