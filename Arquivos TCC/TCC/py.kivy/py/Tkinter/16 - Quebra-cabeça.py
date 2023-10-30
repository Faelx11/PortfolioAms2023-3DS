import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "img/fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -20, y = -55) 

def _init_(self, *args, **kwargs):
    pass



#voltar
photo = PhotoImage(file="img/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=14, y=45)

#img quebra cabeça
photo1 = PhotoImage(file= "img/quebra-cabeca.png")
photo1 = photo1.subsample(8, 8)
figura = Label(image= photo1)
figura.grid(padx=325, pady=30)

#titulo quebra cabeça
txt1 = Label(janela,text = "Quebra-Cabeça", fg="#B457FE", font=('Century Gothic',22))
txt1.place(x=75, y=45)

#upload
btn1 = Button(janela, bd=0, text="Fazer upload de\nimagem",bg="#C985FF")
btn1.place(x=130, y=450,width=150, height=35)

#imprimir
btn2 = Button(janela, bd=0, text="Pronto para imprimir",bg="#C985FF")
btn2.place(x=130, y=550,width=150, height=35)



janela.mainloop()
Place()