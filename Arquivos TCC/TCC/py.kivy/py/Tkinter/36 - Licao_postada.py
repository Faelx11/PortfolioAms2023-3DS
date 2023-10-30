import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)

def _init_(self):
    pass



#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=12, y=45)


#DESCRIÇÃO DA ATIVIDADE
txt1 = Label(janela,text = "DESCRIÇÃO DA\nATIVIDADE", fg="#000000", font=('Century Gothic',20))
txt1.place(x=100, y=65)

#upload
btn1 = Button(janela, bd=0,text="                  ",  bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=60, y=150,width=280, height=450)

#upload
photo2 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo2 = photo2.subsample(17, 17)
btn1 = Button(janela, bd=0,text="postar", image= photo2, bg="#C3FF93", compound= RIGHT, font=('Century Gothic',16))
btn1.place(x=120, y=620,width=170, height=45)

janela.mainloop()
Place()