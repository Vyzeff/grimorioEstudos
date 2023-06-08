# EXERCICIO 09
# Determinar se um avião pode chegar no local de destino com base na distancia e com base no peso dele.
# Testes automatizados.

# d=√((x2 – x1)² + (y2 – y1)²).

from math import sqrt

cargoKg = int(input())
pointAX = int(input())
pointAY = int(input())
pointBX = int(input())
pointBY = int(input())

if (cargoKg <= 50000):
    autonomy = 18000
elif (cargoKg <= 200000):
    autonomy = 9000
else:
    autonomy = 3000

autonomyConditional = autonomy + (autonomy*0.1)
distance = sqrt(((pointBX - pointAX)**2) + ((pointBY - pointAY)**2))

if (distance > autonomyConditional):
    canDistance = "NAO"
elif(distance <= autonomyConditional and distance > autonomy):
    canDistance = "TALVEZ"
else:
    canDistance = "SIM"

print(f"{distance:0.2f}")
print(canDistance)