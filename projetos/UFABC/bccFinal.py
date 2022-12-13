import csv
import numpy as np
import pandas as pd
    
#Porem, tive dificuldade em fazer o csv abrir um link como https://drive.google.com/uc?export=download&id=10zM8jUJZtelgky9Zh5QvPsEI1yxUiy13, então
#os dados foram extraídos separadamente.
#Considerando 0 como um diagnostico positivo para a doença e 1 como a presença do sintoma, temos:

def csvFindHeavierColumn(csvFile, csvColumn):
    #start pandas and read file
    df = pd.read_csv(csvFile, sep=',', dtype=int);
    #get dataframe columns
    dataColumns = df.columns
    #start dict to store corr values
    corrList = {}

    colunas = {"ciclo" : 0, "mem_min" : 0, "mem_max" : 0, "cache" : 0, "min_canais" : 0, "max_canais" : 0}
    dictKeys = list(colunas.keys())

    for x in range(len(dictKeys)):
        colunas[dictKeys[x]] = df[csvColumn].corr(df[dictKeys[x]])

    print(colunas)
    maxCorr = max(colunas.values())
    print(f"A coluna com a maior correlação com {csvColumn} é {maxCorr}")
    return 0

def main():
    csvFindHeavierColumn('computadores_rotulos.csv', 'performance')

# Main function calling
if __name__ == "__main__":
    main()
    


    #for column in dictKeys:
    #    if column != csvColumn:
    #        print(column)
    #       colunas["{column}"] = df[csvColumn].corr(df[column])