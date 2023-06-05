# EXERCICIO 06
# Comparar duas datas
# Testes automatizados.

from datetime import datetime

def comparar_datas(d1, m1, a1, d2, m2, a2):
    """     
        Retorna -1 se a data1 é a mais antiga;
        Retorna 0 se as duas datas são iguais;
        Retorna 1 se as data2 é a mais antiga.
    """
    date01 = datetime(a1,m1,d1)
    date02 = datetime(a2,m2,d2)
    if (date01 > date02):
        return 1
    elif (date01 == date02):
        return 0
    else:
        return -1    

