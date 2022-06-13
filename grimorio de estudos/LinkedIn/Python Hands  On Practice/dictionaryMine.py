def createDict(name):
    try:
       f = open(name, "x")
    except:
        print("Something went wrong.")
        return 1
    f.close()
    choice3 = input("File created. Do you now want to write to your file? ").lower()
    
    if choice3 == "y" or choice3 == "yes":
        writeDict(name)
    else:
        print("Operation complete.")
    return 0
        
def writeDict(name):
    
    key = input("Your key: ")
    val = input("Your value: ")
    
    with open(name, "a") as f:
            f.write(f"{key}: {val}\n")

    choice2 = input("Do you want to write more? ").lower()
    if choice2 == "y" or choice == "yes":
        writeDict(name)
    else:
        print("Your file has been saved. ")
    return 0
def readDict(name):
    with open(name, "r") as f:
        return print(f.read())
        


if __name__ == "__main__":
    name = input("What is your file called? ")
    choice = input("Great! Now, do you want to READ that file, WRITE to that file or CREATE the file?")
    
    if choice == "CREATE":
        createDict(name)
        
    elif choice == "WRITE":
        writeDict(name)
    
    elif choice == "READ":
        readDict(name)
        
    else:
        print("\nSorry, I did not understand. Please try again.")
        
