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

#login
photo1 = PhotoImage(file="img/login.png")
photo1 = photo1.subsample(15, 15)
btn1 = Button(janela, bd=0, image=photo1, text="")
btn1.place(x=350, y=10)
txt1 = Label(janela,text = "Login", fg="black", font=('Century Gothic',7))
txt1.place(x=356, y=47)

#conteudo
photo2 = PhotoImage(file="img/conteudo.png")
photo2 = photo2.subsample(2, 2)
txt2 = Label(janela,text = "Conteudo", fg="black", font=('Century Gothic',20))
txt2.place(x=125, y=480)
btn2 = Button(janela, bd=0, image=photo2, text="")
btn2.place(x=80, y=200)



janela.mainloop()
Place()