import re

def findPalindrome(input):

    treatedString = ''.join(re.findall(r"[a-z]+", input.lower()))
    
    if treatedString == treatedString[::-1]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    string = input("Please give me a string and I will say if it is a palindrome or not.\n")
    print(findPalindrome(string))