def factor():
    
    print("I will find the prime factors of any number you give me.\n")
    
    try:
        userInput = int(input("Please give me a number: "))
    
    except ValueError:
        print("Please input a valid number. Try again.")
        return 1
    
    divisible = {}
    for num in range(2, userInput):
        if userInput % num == 0:
            divisible[num] = True
            
    for x in divisible:
        for z in range(2, x):
            if x % z == 0:
                divisible[x] = False
                
    for x in divisible:
        if divisible[x] == True:
            print(x, end=", ")
    print("")
    return 0

if __name__ == "__main__":
    factor()