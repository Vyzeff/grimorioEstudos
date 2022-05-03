

#   Importa random para gerar um numero enter 1 e 20, enquanto o modulo time serve para criar um delay na resposta.
import random
import time

def d20():
    global run  #   Fala para run ser global e que possa ser detectado depois por msg()

    run = True  #   Valor bool que enquanto for verdade, o loop ira continuar
    resposta = 0
    print("Bem vindo.")
    while run:

        print("Se deseja jogar um dado d20, digite um número. Se deseja acabar com a simulação, digite qualquer outra coisa.")

        try:
            resposta = int(input())
        except ValueError:      #   Checa pelo valor do input do jogador, onde somente se um numero for digitado a interação
            run = False         #   em else vai ocorrer. Caso contrário, break ira ocorrer.
            break
        else:
            number = random.randint(1,20)
            print("O dado é jogado... ")
            time.sleep(1)       #   Causa um delay de 1s para o próximo comando.
            print("e o resultado é:")
            time.sleep(2)
            print(number)
            

def msg():
    if not run:
        print("Obrigado por utilizar desta simples programa.")

d20()

msg()

print(input("Precione Enter para fechar o aplicativo."))