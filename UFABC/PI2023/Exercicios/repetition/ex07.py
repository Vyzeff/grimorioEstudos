# EXERCICIO 07
# Ler um valor N e então mostre os N primeiros números primos
# Testes automatizados.
# bem dificil na verdade
desiredPrimes = int(input())

primeList = [2]
initPrime = 3  
while len(primeList) < desiredPrimes:
    isPrime = True
    for i in range(len(primeList)):
        if initPrime % primeList[i] == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(initPrime)
    initPrime += 2

for i in range(len(primeList)):
    print(primeList[i])
