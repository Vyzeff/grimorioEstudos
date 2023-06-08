# EXERCICIO 09
# VCom base em um número de 6 digitos, dizer de onde o disco voador veio.
# Testes automatizados.

# OODDMM:

#     OO: código do planeta de origem (onde o disco voador foi fabricado)
#     DD: código do planeta de destino (onde o disco voador será entregue)
#     MM: código do modelo

# A empresa usa as seguintes tabelas com os códigos de planetas e modelos de discos voadores:
# Código 	Planeta
# 80 	Marte
# 81 	Saturno
# 90 	Netuno
# 91 	HD21749b


# Código 	Modelo
# 60 	A6000
# 61 	B7500
# 62 	C9000


discNumber = input()

originPlanetCode = int(discNumber[0] + discNumber[1])
destinyPlanetCode = int(discNumber[2] + discNumber[3])
modelCode = int(discNumber[4] + discNumber[5])

if (originPlanetCode == 80):
    originPlanet = "Marte"
elif (originPlanetCode == 81):
    originPlanet = "Saturno"
elif (originPlanetCode == 90):
    originPlanet = "Netuno"
else:
    originPlanet = "HD21749b"

if (destinyPlanetCode == 80):
    destinyPlanet = "Marte"
elif (destinyPlanetCode == 81):
    destinyPlanet = "Saturno"
elif (destinyPlanetCode == 90):
    destinyPlanet = "Netuno"
else:
    destinyPlanet = "HD21749b"

if (modelCode == 60):
    model = "A6000"
elif (modelCode == 61):
    model = "B7500"
else:
    model = "C9000"

print(originPlanet)
print(destinyPlanet)
print(model)