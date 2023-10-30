import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -20, y = -35) 

def _init_(self):
    pass



#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=12, y=45)

#Pc-imagem
photo1 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc-imagem.png")
photo1 = photo1.subsample(5, 5)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=310, pady=15)

#Palavras Cruzadas
txt1 = Label(janela,text = "Palavras\nCruzadas", fg="#000000", font=('Century Gothic',20))
txt1.place(x=140, y=15)

#Texto 
txt2 =Label (janela,bd=0,text = "Estão disponiveis três\nníveis de palavras\ncruzadas para a\nimpressão: nível fácil(1\na 5 palavras), nível\nmédio (de 5 a 10\npalavras), e o nível\ndifícil (contendo mais\nde 10 palavras).", fg="#000000", font=('Century Gothic',15), justify= LEFT, anchor=W, )
txt2.place(x=95, y=200,)

#Imagem Imprimir
photo2 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Img-Imprimir.png")
photo2 = photo2.subsample(15, 15)

#acessar
btn1 = Button(janela, bd =0,text="Acessar",image= photo2, bg="#C3FF93", compound= RIGHT, font=('Century Gothic',12))
btn1.place(x=110, y=480,width=190, height=45)

janela.mainloop()
Place()