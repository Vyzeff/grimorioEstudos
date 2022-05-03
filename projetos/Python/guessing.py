#   In this project, my goal is to create a simple game of number guessing, where the terminal will choose randomly a number
# between 1 and 100 and the player will have to guess correctly. For each wrong guess, there is a tip. Maybe a bigger or
# smaller number, or even if it is a multiple to some other number.

#   Importa o módulo random, usado para gerar o número aleatório

import random

#   Gera o número base do jogo, define variaveis



#   O jogo inteiro dentro de um loop, onde se o jogador acertar ou passar do numero de tentativas, o jogo para.

def guess():

    global acertou          #   Define o resultado, se o jogador acertou ou não, como global

    #   Define a diferença maxima, que é onde o numero random vai ser criado
    ceiling = random.randint(1, 350)
    number = random.randint(1, ceiling)

    print("Mano, me fala um número entre 1 e {}, você tem 7 chances." .format(ceiling))

    count = 1
    chute = 0
    acertou = False
        
    #   O loop funciona enquanto o bool acertou for falso, que só é mudado quando o chute, que seria o input do jogador, é
    # igual ao numero escolhido
    while not acertou:
        try:
            chute = int(input())
        except ValueError:
            print("Acho que você não me entendeu, isso não é um número, e estamos falando deles.")
            print("Tenta de novo.")
        else:
            if (chute == number):
                acertou = True
                break
            #   Se a acontagem, que é encrementada a cada chute, chegar a 7, 
            elif (count == 7):
                break
            if (count == 4):
                print("Cuidado em, pensa direito que você passou da metade das suas tentavivas...")
            if (count == 6):
                print("Ultima tentativa, usa todo esse seu cérebro ai.")
                count = count + 1

            else:       #   Dependendo do chute, define a dica, e encrementa a contagem
                if (chute < number):
                    print("Jogou muito baixo. Tenta um número maior.")
                else:
                    print("Foi lá pro alto. Tenta mais baixo.")
                count = count + 1

def msg ():         #   Mensagem que é chama depois da finalização do jogo, depende do valor do bool acertou
    if acertou:
        print("Mano, eu real não esperava. Parabéns por acertar o número.")
    else:
        print("Infelizmente você não conseguiu acertar o número mano, tenta melhor na próxima.")


guess()
msg()

print(input("Obrigado por jogar, precione Enter para fechar."))     #   Input para manter o terminal aberto