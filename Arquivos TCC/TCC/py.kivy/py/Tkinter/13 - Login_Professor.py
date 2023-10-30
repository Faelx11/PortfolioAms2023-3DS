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

#txt LOGIN
txt1 = Label(janela,text = "LOGIN", fg="black", font=('Century Gothic',30))
txt1.place(x=145, y=75)

#nome
txt2 = Label(janela,text = "NOME:", fg="black", font=('Century Gothic',20))
txt2.place(x=30, y=180)
entrada = Entry(janela,bg="#77C4FF")
entrada.place(x=135, y=185,width=240, height=35)

#email
txt3 = Label(janela,text = "EMAIL:", fg="black", font=('Century Gothic',20))
txt3.place(x=30, y=240)
entrada1 = Entry(janela,width=35,bg="#77C4FF")
entrada1.place(x=135, y=245,width=240, height=35)

#senha
txt4 = Label(janela,text = "SENHA:", fg="black", font=('Century Gothic',20))
txt4.place(x=30, y=300)
entrada2 = Entry(janela,width=35,bg="#77C4FF")
entrada2.place(x=135, y=305,width=240, height=35)

#realizar login
btn1 = Button(janela, bd=0, text="Realizar Login",bg="#77C4FF", font=(20))
btn1.place(x=130, y=425, width=150, height=35)




janela.mainloop()
Place()