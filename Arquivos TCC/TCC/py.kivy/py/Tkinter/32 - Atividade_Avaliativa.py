import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "py.kivy/py/img_wireframe\ICONS\Atividade-A\Fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -20, y = -55) 

def _init_(self):
    pass



#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=12, y=45)

#img atividade avaliativa
photo1 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Atividade-A\Icone.png")
photo1 = photo1.subsample(5, 5)
figura = Label(image= photo1)
figura.grid(padx=315, pady=15)

#Atividade Avaliativa
txt1 = Label(janela,text = "Atividade\nAvaliativa", fg="#000000", font=('Century Gothic',20))
txt1.place(x=130, y=15)

#Botão
btn1 = Button(janela, bd =0,text="Fazer Upload de\nImagem", bg="#77C4FF", compound= RIGHT, font=('Century Gothic',12))
btn1.place(x=110, y=480,width=190, height=45)

janela.mainloop()
Place()