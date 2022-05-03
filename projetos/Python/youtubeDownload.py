# WIP

from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests


# Define o básico da janela.

root = tk.Tk()
root.title("Youtube Video Downloader")
root.config(bg= "coral")
root.geometry("300x300")


#   Centraliza a janela quando aberta

winWidth = root.winfo_reqwidth()  #  Retorna os tamanhos da propria janela, definidos em window.configure
winHeight = root.winfo_reqheight()
posLeft = int(root.winfo_screenwidth() / 2.5 - winWidth / 2)
posUp = int(root.winfo_screenheight() / 3 - winHeight / 2) 
root.geometry("600x440+{}+{}" .format(posLeft, posUp))

# Define as colunas e rows da grid onde os widgets irao se encontrar

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight =  1)
root.columnconfigure(2, weight =  1)
root.columnconfigure(3, weight =  1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)

def linkClick():
    l1 = Label(root, text="FUNCIONOU O LINK, ELE É " + link.get())
    l1.pack(anchor = CENTER)

 

buttonCall = Button(
    root,
    bd="0",
    fg = "dimgray",
    activeforeground = "silver",
    activebackground = "mistyrose",  
    bg = "mistyrose", 
    text = "Opções de Download", 
    font = "roboto 12",
    command = linkClick
)
buttonCall.grid(row = 2, column = 2, columnspan = 2)

linkLabel = Label(
    root,
    text = "Após confirmar que o link é do vídeo desejado, clique no botão a baixo.",
    font = "roboto 12",
    background = "coral",
    )
linkLabel.pack(side = BOTTOM)

link = tk.StringVar()
linkEntered = ttk.Entry(root, width ="95", textvariable = link)
linkEntered.grid(row = 0, column = 0, columnspan = 2)
linkPlaceholder = Button(
    root, 
    bd="0",
    activebackground = "coral",  
    bg = "coral", 
    padx = 450
)
linkPlaceholder.pack()



buttomDownload = Button(
    root, 
    bd="0",
    fg = "dimgray",
    activeforeground = "silver",
    activebackground = "mistyrose",  
    bg = "mistyrose", 
    text = "Faça seu Download", 
    font = "roboto 15",
    )
buttomDownload.pack()
buttomPlaceholder = Button(
    root, 
    bd="0",
    activebackground = "coral",  
    bg = "coral", 
    padx=100
    )
buttomPlaceholder.grid(row = 3, column = 1, columnspan = 2)


# #   Mantém a janela aberta
root.mainloop()