from tkinter import *

janela = Tk ()
rotulo = Label(janela,text="olá mundo")
rotulo.grid(row=0, collumn=0)

rotulo2 = Label(janela, text="Tudo bem?")
rotulo2.grid(row=1, column=0)



botao_sair = Button(janela)
botao_sair.grid(row=1, column=0)
botao_sair ["text"] = "Sair"
botao_sair ["width"] = 10
botao_sair ["command"] = quit




janela.mainloop()