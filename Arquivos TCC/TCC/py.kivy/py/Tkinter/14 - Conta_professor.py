import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)


def _init_(self):
    pass



#voltar
photo = PhotoImage(file="img/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=14, y=45)

#img professor(a)
photo1 = PhotoImage(file= "img/Jaqueline_Maciel.png")
photo1 = photo1.subsample(3,3)
figura = Label(image= photo1)
figura.grid(row=0, column=0, padx=100, pady=70)

#nome professor(a)
txt1 = Label(janela,text = "profª: Jaqueline Maciel", fg="black", font=('Century Gothic',20))
txt1.place(x=50, y=290)

#conteudo
btn1 = Button(janela, bd=0, text="Conteúdo",bg="#B4DE60")
btn1.place(x=130, y=420,width=150, height=35)


janela.mainloop()
Place()