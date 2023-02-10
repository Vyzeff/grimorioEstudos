#WIP

import random
from time import sleep

def slice():
    print("Obrigado por escolher nosso programa para seu uso.") 
    email = input("Por favor, escreva um email valido.")
    normalUser = email[:email.index("@")]                                                                   
    normalDomain = email[:email.index("@")]
    print("Seu nome de usuário recomendado seria...")
    sleep(1)
    print(normalUser + str(random.randint(1,99)))
    sleep(2)
    print("Seu domínio recomendado seria...")
    print(normalDomain.replace(".", "") + ".com.br")
    input("Obrigado por usar nossos serviços. Finalizando... Precione Enter para fechar.")

    
slice()