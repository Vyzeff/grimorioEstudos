# EXERCICIO 07
# Revisão de disco voadores
# Testes automatizados.

prodYear = int(input())
motorCode = int(input())
distanceTravel = int(input())


if (prodYear >= 2021):
    if (motorCode in [200, 201] and distanceTravel > 200):
        print("SIM")
    else: 
        print("NAO")
elif(prodYear >= 2001):
    if(distanceTravel > 5000):
        print("SIM")
    else:
        print("NAO")
elif(prodYear >= 1901):
    if(motorCode in [100, 101]):
        print("SIM")
    else:
        print("NAO")
else:
    print("NAO")