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

txt1 = Label(janela,text = "Conteúdo", fg="black", font=('Century Gothic',30))
txt1.place(x=100, y=75)

#avaliar atividades
photo1 = PhotoImage(file="img/avaliacao.png")
photo1 = photo1.subsample(5, 5)
txt2 = Label(janela,text = "Consultar Progresso", fg="black", font=('Century Gothic',12))
txt2.place(x=24, y=288)
btn2 = Button(janela, bd=0, image=photo1, text="")
btn2.place(x=58, y=180)


#matematica
photo2 = PhotoImage(file="img/matematica.png")
photo2 = photo2.subsample(5, 5)
txt3 = Label(janela,text = "Matemática", fg="black", font=('Century Gothic',12))
txt3.place(x=257, y=288)
btn3 = Button(janela, bd=0, image=photo2, text="")
btn3.place(x=258, y=180)

#Palavras Cruzadas
photo3 = PhotoImage(file="img/palavras-cruzadas.png")
photo3 = photo3.subsample(5, 5)
txt4 = Label(janela,text = "Palavras Cruzadas", fg="black", font=('Century Gothic',12))
txt4.place(x=35, y=470)
btn4 = Button(janela, bd=0, image=photo3, text="")
btn4.place(x=58, y=360)

#Pintura
photo4 = PhotoImage(file="img/pintura.png")
photo4 = photo4.subsample(5, 5)
txt5 = Label(janela,text = "Pintura", fg="black", font=('Century Gothic',12))
txt5.place(x=282, y=470)
btn5 = Button(janela, bd=0, image=photo4, text="")
btn5.place(x=258, y=360)

#Quebra-Cabeça
photo5 = PhotoImage(file="img/quebra-cabeca.png")
photo5 = photo5.subsample(5, 5)
txt6 = Label(janela,text = "Quebra Cabeça", fg="black", font=('Century Gothic',12))
txt6.place(x=137, y=648)
btn6 = Button(janela, bd=0, image=photo5, text="")
btn6.place(x=154, y=540)






janela.mainloop()
Place()