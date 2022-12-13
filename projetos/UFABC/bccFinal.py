import pandas as pd
    
def csvFindHeavierColumn(csvFile = 'computadores_rotulos.csv', csvColumn = 'performance'):
    
    #com pandas, ler o arquivo csv
    df = pd.read_csv(csvFile, sep=',', dtype=int);
    
    #get dataframe columns
    nomeColunas = df.columns
    
    #start dict to store corr values
    corrLista = {}
    
    for coluna in nomeColunas:
        try:
            if coluna != csvColumn:
                corrLista[coluna] = df[csvColumn].corr(df[coluna])
        except:
            break
    
    print(f"A lista total de correlações do arquivo {csvFile} segue:")
    for data in corrLista:
        print(f"{data}: {corrLista[data]:0.3f}")


    return 0

def main():
    csv = input("Por favor, um csv ou link para csv: ")
    coluna = input("Por fim, digite a coluna desejada para os calculos: ")
    try:
        csvFindHeavierColumn(csv, coluna)
    except:
        print("Por favor, verifique se você digitou corretamente os dados e tente novamente.")
# Main function calling
if __name__ == "__main__":
    main()
