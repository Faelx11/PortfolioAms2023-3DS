import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "img/fundoP.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -50, y = -1) 

def _init_(self, *args, **kwargs):
    pass



#voltar
photo = PhotoImage(file="img/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=14, y=45)

#img pintura
photo1 = PhotoImage(file= "img/pintura.png")
photo1 = photo1.subsample(8, 8)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=325, pady=30)

#titulo pintura
txt1 = Label(janela,text = "Pintura", fg="#000000", font=('Century Gothic',22))
txt1.place(x=150, y=45)

#Texto 
txt2 =Label (janela,bd=0,text = "Estão disponiveis três\ntipos de modelos de\npintura para a\nimpressão: Animais,\nAlimentos e sobre as\ncores.", fg="#000000", font=('Century Gothic',14), justify= LEFT, anchor=W)
txt2.place(x=100, y=200,)

#Imagem Imprimir
photo2 = PhotoImage(file="img_wireframe\ICONS\Pc-Imprimir\Img-Imprimir.png")
photo2 = photo2.subsample(15, 15)

#botao acessar
btn1 = Button(janela, bd =0,text="Acessar",image= photo2, bg="#77C4FF", compound= RIGHT,  font=('Century Gothic',12))
btn1.place(x=110, y=480,width=190, height=45)


janela.mainloop()
Place()