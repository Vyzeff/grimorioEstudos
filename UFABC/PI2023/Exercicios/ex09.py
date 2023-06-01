#   EXERCICIO 09
# Calcular o numero de caixar baseado na capacidade maxima de um caminhão
# Testes automatizados.

truckCap = int(input())

fiveCrates = truckCap // 500
truckCap -= 500*fiveCrates

hundredCrates = truckCap // 100
truckCap -= 100*hundredCrates

twentyCrates =  truckCap // 25
truckCap -= 25*twentyCrates

oneCrates =  truckCap // 1
truckCap -= 1*oneCrates

print(fiveCrates)
print(hundredCrates)
print(twentyCrates)
print(oneCrates)