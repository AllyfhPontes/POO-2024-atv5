from cProfile import label
from email import message
from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Boas vindas")
janela.geometry ("300x200+100+100")

rotulo = Label(janela, text="qual o seu nome?")
rotulo.grid(row=0, column=0)

campo = Entry(janela)
campo.grid(row=1,column=1)

def boasvindas():
    messagebox.showinfo(message="seja bem vindo!")

botao = Button(janela, text="Enviar")
botao.grid(row=1,column=0)
botao["text"] = "enviar"
botao["command"] = boasvindas

janela.mainloop()