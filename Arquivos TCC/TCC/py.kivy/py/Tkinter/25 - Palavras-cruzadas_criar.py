import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -20, y = -35) 

def _init_(self, *args, **kwargs):
    pass



#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=14, y=45)

#Palavras Cruzadas
txt1 = Label(janela,text = "Palavras\nCruzadas", fg="#000000", font=('Century Gothic',20))
txt1.place(x=140, y=15)

#img palavras cruzadas
photo2 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc.png")
photo2 = photo2.subsample(2, 2)
figura = Label(image= photo2)
figura.grid(row=0, column=0, padx=75, pady=210)

#upload
photo3 = PhotoImage(file="py.kivy/py\img_wireframe\ICONS\Matematica\Subir.png")
photo3 = photo3.subsample(17, 17)
btn1 = Button(janela, bd=0,text="Upload", image= photo3, bg="#C3FF93", compound= RIGHT, font=('Century Gothic',12))
btn1.place(x=120, y=500,width=170, height=45)

janela.mainloop()
Place()