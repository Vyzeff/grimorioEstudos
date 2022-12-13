import pandas as pd
import numpy as np
from math import ceil
from random import randint
def csvFindRelations(csvFile = 'computadores_rotulos.csv', csvColumn = 'performance', loop=False):
    print(f"Tabela: {csvFile} \nColuna Alvo: {csvColumn}", end="\n \n")
    #com pandas, ler o arquivo csv
    df = pd.read_csv(csvFile, sep=',', dtype=int);
    
    #pegar nomes das colunas do banco de dados
    nomeColunas = df.columns
    
    #começar um dicionario para as correlações e as colunas
    corrLista = {}
    
    #para cada coluna, fazer uma correlação com a coluna escolhida
    for coluna in nomeColunas:
        #tentar fazer a correlação, se der erro, saia do loop
        try:
            if coluna != csvColumn:
                corrLista[coluna] = df[csvColumn].corr(df[coluna])
        except:
            break
    
    #printa a lista de correlações com 3 numeros apos o 0
    print(f"A lista total de correlações do arquivo {csvFile} segue:")
    for data in corrLista:
        print(f"{data}: {corrLista[data]:0.3f}")
        
    #calcula e printa a media de todas as correlações atuais
    primeiraMedia = np.median(list(corrLista.values()))
    print(f"A media de todas as correlações com {csvColumn} é de {primeiraMedia:0.3f}.", end="\n \n")
    
    #pega a correlação maxima e minima da lista
    maxCorr =  max(corrLista, key=corrLista.get)
    minCorr = min(corrLista, key=corrLista.get)
    
    #arredonda o maximo e verifica o grau da correlação
    if ceil(corrLista[maxCorr]) >= 0.7:
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma forte correlação de {corrLista[maxCorr]}")
    elif ceil(corrLista[maxCorr]) >= 0.4: 
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma media correlação de {corrLista[maxCorr]}")
    else:
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma fraca correlação de {corrLista[maxCorr]}")

    #printa a menor correlação achada
    print(f"A menor correlação entre todas com {csvColumn} é aquela de {minCorr}, com uma fraca relação de {corrLista[minCorr]}", end="\n \n")

    #se a variavel loop for falsa, executa a função
    if loop == False:
        print("Segue, tambem, uma outra relação completamente aleatória.")
        randValue = randint(0, len(nomeColunas) -1)
        csvFindRelations(csvFile, nomeColunas[randValue], loop=True)
    return 0

def main():
    csv = input("Por favor, um csv ou link para csv: ")
    coluna = input("Por fim, digite a coluna desejada para os calculos: ")
    try:
        csvFindRelations(csv, coluna)
    except:
        print("Por favor, verifique se você digitou corretamente os dados e tente novamente.")
# Main function calling
if __name__ == "__main__":
    main()
