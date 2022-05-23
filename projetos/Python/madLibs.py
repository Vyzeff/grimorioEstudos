# Mad Libs é um jogo onde o participante escreve uma serie de palavras aleatórias baseadas na pergunta e recebe uma história
# Além do jogo, que é basicamente feito com input()s e print()s, também vou adicionar uma janela própria com botões


## Janela Customizavel --------------------------------------------------------------------------------------------------

#   importa tkinter para a janela customizavel

from tkinter import *

#   Define o objeto da janela, configura o básico e adiciona texto

window = Tk()
window.title("Mad Libs Project")
window.config(bg = "seagreen")
window.geometry("")

#   Centraliza a janela quando aberta

winWidth = window.winfo_reqwidth()  # Retorna os tamanhos da propria janela, definidos em window.configure
winHeight = window.winfo_reqheight()
posLeft = int(window.winfo_screenwidth() / 2.5 - winWidth / 2)
posUp = int(window.winfo_screenheight() / 3 - winHeight / 2) 
window.geometry("600x450+{}+{}" .format(posLeft, posUp))

#   Escreve textos na janela e os anchora ao centro

lb1 = Label(window, text = "Welcome",bg = "seagreen", fg = "darkkhaki", font = "roboto 30")
lb2 = Label(window, text = "---Select your theme---", bg = "seagreen", fg = "darkkhaki", font = "roboto 20", bd = "20")
lb1.config(anchor=CENTER)
lb1.pack()
lb2.config(anchor=CENTER)
lb2.pack()

#   Define as opções de texto

def Pot():
    characteristic = input("Give me a characteristic: ")
    colour = input("How about a colour: ")
    hunger = input("By the way, how hungry are you? ")
    number = input("And for no reason at all, give me a number between 0 and 10: ")
    print("The " + characteristic + " pot was " + colour + " after cooking. I was lucky it was already hot before I put in all the " + number + " potatoes in there, after all, I was " + hunger)

def Hobbies():
    games = input("Trick question, do you like to play games? ")
    reading = input("And what about reading an interesting book? ")
    music = input("Or  how about your favourite genre of music? ")
    print("I see, you " + games + ". Can't say I agree. Personally, I really like playing then, but I agree on " + reading + " books. And thats really something, liking " + music + ". I can't stand it.")

def Sports():
    exercise = input("Hmm, what is your favourite type of exercise? ")
    fit = input("In one word, describe how fit you are right now: ")
    weight = input("How much can you lift with one hand?")
    print("Personally, I don't like " + exercise + ". I'm more of a legs guy you know? Running, squats and all of that is what I do. Once, I was " + fit + " like you, but in the quarentine, things changed a lot. For example, from " + weight + " I could lift, I'm now around 25kg.")

#   Define os botões que irão realizar o comando ao serem clicados e os anchora ao centro

b1 = Button(window, text = "Cooking Pot", font = "roboto 25", bg = "aquamarine", command = Pot)
b1.config(anchor=CENTER)
b1.pack()

b2 = Button(window, text = "Hobbies", font = "roboto 25", bg = "aquamarine", command = Hobbies)
b2.config(anchor=CENTER)
b2.pack()

b3 = Button(window, text = "Sports", font = "roboto 25", bg = "aquamarine", command = Sports)
b3.config(anchor=CENTER)
b3.pack()

#   Abre a Janela e a mantem

window.mainloop()