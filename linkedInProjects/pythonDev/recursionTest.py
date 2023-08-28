# Using recursion to implement power and factorial functions


def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)

print(f"5 to the power of 3 is {power(5,3)}")

powerNum = int(input("O numero para ser elevado: "))
powerPower = int(input("O número de vezes que deve ser elevado: "))

print(f"{powerNum} to the power of {powerPower} is {power(powerNum, powerPower)}", )
print(f"4! is {factorial(4)}")

factNum = int(input("The factorial: "))

print(f"{factNum}! is {factorial(factNum)}")
