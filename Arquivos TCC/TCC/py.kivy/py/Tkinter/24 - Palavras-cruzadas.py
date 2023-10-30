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

#Pc-imagem
photo1 = PhotoImage(file= "py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc-imagem.png")
photo1 = photo1.subsample(5, 5)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=310, pady=15)

#Palavras Cruzadas
txt1 = Label(janela,text = "Palavras\nCruzadas", fg="#000000", font=('Century Gothic',20))
txt1.place(x=140, y=15)

#upload
btn1 = Button(janela, bd=0, text="Fazer upload de\nimagem",bg="#C3FF93")
btn1.place(x=130, y=450,width=150, height=35)

#imprimir
btn2 = Button(janela, bd=0, text="Pronto para imprimir",bg="#C3FF93")
btn2.place(x=130, y=550,width=150, height=35)



janela.mainloop()
Place()