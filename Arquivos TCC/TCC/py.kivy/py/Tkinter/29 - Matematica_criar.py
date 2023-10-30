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

#titulo Matematica
txt1 = Label(janela,text = "Matemática", fg="#000000", font=('Century Gothic',22))
txt1.place(x=100, y=45)

#imgMatiCriar
photo1 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Matematica\MatiCriar.png")
photo1 = photo1.subsample(2, 2)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=50, pady=190)

#upload
photo2 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo2 = photo2.subsample(17, 17)
btn1 = Button(janela, bd=0,text="Upload", image= photo2, bg="#C985FF", compound= RIGHT, font=('Century Gothic',12))
btn1.place(x=120, y=500,width=170, height=45)


janela.mainloop()
Place()