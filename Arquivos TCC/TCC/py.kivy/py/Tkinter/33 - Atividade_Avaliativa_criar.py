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


#Atividade Avaliativa
txt1 = Label(janela,text = "Atividade\nAvaliativa", fg="#000000", font=('Century Gothic',20))
txt1.place(x=140, y=15)

#img atividade avaliativa criar
photo2 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Atividade-A\Imagem1.png")
photo2 = photo2.subsample(2, 2)
figura = Label(image= photo2)
figura.grid(row=0, column=0, padx=50, pady=190)

#upload
photo3 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo3 = photo3.subsample(17, 17)
btn1 = Button(janela, bd=0,text="Upload", image= photo3, bg="#77C4FF", compound= RIGHT, font=('Century Gothic',12))
btn1.place(x=120, y=500,width=170, height=45)

janela.mainloop()
Place()