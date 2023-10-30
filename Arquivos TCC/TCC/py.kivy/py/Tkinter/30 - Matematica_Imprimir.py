import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -28, y = -35) 

def _init_(self):
    pass



#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=12, y=45)

#img matematica
photo1 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Matematica\Matematica.png")
photo1 = photo1.subsample(5, 5)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=310, pady=30)

#titulo Matematica
txt1 = Label(janela,text = "Matemática", fg="#000000", font=('Century Gothic',22))
txt1.place(x=100, y=45)

#Texto 
txt2 =Label (janela,bd=0,text = "Estão disponiveis\nquatro sessões sobre\nmatemática para a\nimpressão: 1 sessão -\nadição e subtração, 2ª\nsessão - multiplicação\ne divisão.", fg="#000000", font=('Century Gothic',14), justify= LEFT, anchor=W)
txt2.place(x=100, y=200,)

#Imagem Imprimir
photo2 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Img-Imprimir.png")
photo2 = photo2.subsample(15, 15)

#botao acessar
btn1 = Button(janela, bd =0,text="Acessar",image= photo2, bg="#C985FF", compound= RIGHT,  font=('Century Gothic',12))
btn1.place(x=110, y=480,width=190, height=45)

janela.mainloop()
Place()