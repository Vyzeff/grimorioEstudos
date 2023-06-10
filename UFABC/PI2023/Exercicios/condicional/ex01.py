# EXERCICIO 01
# Checar se um vendedor bate a meta em comparação com seu salario
# Testes automatizados.


salary = int(input())
allSales = int(input())

comissionValue = allSales*0.2
print(f"{comissionValue:0.2f}")

if (comissionValue >= salary*0.5):
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")