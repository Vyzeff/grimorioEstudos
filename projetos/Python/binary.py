#   This program will create a list of random numbers between 0 to 100. When the user inputs a random number,
#   the program will check if that number is included in the list. It will do so by creating two halves of the list.
#   If the program finds the number in the first half of the list, it will eliminate the other half and vice versa. 
#   The search will continue until the program finds the number input of the user or until the subarray size becomes 0
#   (this means that the number is not in the list).



import random # Importa o modulo random

# Gera uma lista aleatoria de numeros entre 0 e 100 e seleciona 25. Através de sorted(), a lista e "arrumada" em ordem crescente
randomList = sorted((random.sample(range(0, 101), 25))) 
aim = int(input("Digite o número que você deseja encontrar "))
exist = False

def search(list, aim): # O algoritmo em si, atraves de um ponto central procura o item desejado, no caso o input "aim"
    global exist
    start = 0
    end = len(randomList) - 1

    while start <= end:
        midpoint = start + (end - start)//2
        midvalue = list[midpoint]

        if midvalue == aim: # Quando o valor do numero na posição de midvalue for igual a aim, quebra o loop
            exist = True
            return midpoint
        # Dependendo se o valor de midvalue for menor ou maior que aim, muda o começo ou fim da procura
        elif aim < midvalue:
            end = midpoint - 1
        else:
            start = midpoint +1
    return None
        

def main(): # Executa search()
    print(randomList)
    if exist:
        print("Seu item estava na posição " + search(randomList, aim))
    else:
        print("Seu item não estava na lista gerada.")
    input("Aperte enter para fechar a aplicação.")

main()