#   EXERCICIO 08
#   Encriptar um numero somando +1 em cada um de seus digitos
#   Testes automatizados.
#    finalValue += str((encriptedNumber*(10**(numLengh-x))))


initValue = input()
finalValue = str()
numLengh = len(initValue) - 1
overflowNum = False

for x in range(len(initValue)):
    encriptedNumber = int(initValue[x])

    if(overflowNum):
        encriptedNumber += 1
        overflowNum = False
    else:
        encriptedNumber += 1

    if(encriptedNumber == 10):
        encriptedNumber = 0
        overflowNum = True
    finalValue += str((encriptedNumber))

print(finalValue)