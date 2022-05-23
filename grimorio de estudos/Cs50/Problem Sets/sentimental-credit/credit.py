from cs50 import get_int

def main():

        cardNumber = get_int("Please input your credit card number: ")

        if cardValidation(cardNumber):
            cardCompany(cardNumber)
        else:
            print("INVALID")


def cardValidation(input):
    # Calculates the sum using Luhn's Algorithm
    totalSum = 0
    for x, y in enumerate(reversed(str(input))):
        if x % 2 == 0:
            totalSum += int(y)
        else:
            for z in str(int(y) * 2):
                totalSum += int(z)

    # Checks if sum is % by 10
    if totalSum % 10 == 0:
        return True
    else:
        #print("INVALID")
        return False

def cardCompany(input):
    # Gets first two numbers of input
    number = int(str(input)[0:2])

    # Checks for known company
    if number == 34 or number == 37:
        print("AMEX")
    if number >= 40 and number < 50:
        print("VISA")
    if number > 50 and number < 56:
        print("MASTERCARD")
    # Else there is no company, INVALID



if __name__ == "__main__":
    main()