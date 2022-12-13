import pandas as pd
import numpy as np
from math import ceil
from random import randint
import matplotlib.pyplot as plt
%matplotlib inline

#Link para a tabela de computadores: https://drive.google.com/uc?export=download&id=1D605NkuC-c5uh5L0iErZ00bFB6wGiz-F
#Link para tabela de imoveis: https://drive.google.com/uc?export=download&id=1CN8AMb-XoRn5EvpzwKSJHDZiU6mBSHB6
#Atualmente, a tabela de imoveis não funciona por conta dos números serem separador por virgulas, o que quebra o pandas
#Por enquanto, em teoria é possivel usar qualquer tabela que tenha somente números separados por . em suas colunas.

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
    print(f"A lista total de correlações do arquivo {csvFile} segue com a coluna {csvColumn}:")
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
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma forte correlação de {corrLista[maxCorr]:0.3f}")
    elif ceil(corrLista[maxCorr]) >= 0.4: 
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma media correlação de {corrLista[maxCorr]:0.3f}")
    else:
        print(f"A maior correlação de {csvColumn} é {maxCorr}, com uma fraca correlação de {corrLista[maxCorr]:0.3f}")

    #printa a menor correlação achada
    print(f"A menor correlação entre todas com {csvColumn} é aquela de {minCorr}, com uma fraca relação de {corrLista[minCorr]:0.3f}", end="\n \n")

    #plotar os valores de csvColumn em x e de maxCorr em y
    plt.plot(df[csvColumn], df[maxCorr], '.')

    #achar os valores de a e b na reta de ax + b entre as variaveis csvColumn e maxCorr
    (aVariavel, bVariavel) = np.polyfit(x = df[csvColumn], y = df[maxCorr], deg = 1)

    #gera o inicio e fim de x no grafico com base no valor minimo e maximo de csvColumn
    x = np.arange(df[csvColumn].min(), df[csvColumn].max())

    #gera os valores de y para a função de regressao ax + b
    y = aVariavel * x + bVariavel

    #coloca lagendas no grafico e o cria
    plt.title("Regreção Linear")
    plt.xlabel(csvColumn)
    plt.ylabel(maxCorr)
    plt.plot(x, y)

    print(f"Por fim, segue um gráfico da regressão linear entre {csvColumn} e {maxCorr}, contando que numa reta ax + b, a e b nessa \n reta de regressão seriam {aVariavel:0.3f}x + {bVariavel:0.3f}:")

    #mostra o grafico para o usuario e depois o limpa para o proximo uso
    plt.show()
    plt.clf()

    #se a variavel loop for falsa, executa a função novamente com um csvColumn aleatorio
    if loop == False:
        print("Segue, tambem, uma outra relação completamente aleatória.")
        randValue = randint(0, len(nomeColunas) -1)
        csvFindRelations(csvFile, nomeColunas[randValue], loop=True)
    return 0

def main():
    #espera o input do usuario para a tabela e a csvColumn
    csv = input("Por favor, um csv ou link para csv: ")
    coluna = input("Por fim, digite a coluna desejada para os calculos: ")
    try:
      csvFindRelations(csv, coluna, False)
    except:
        print("Por favor, verifique se você digitou corretamente os dados e tente novamente.")
# Main function calling
if __name__ == "__main__":
    main()