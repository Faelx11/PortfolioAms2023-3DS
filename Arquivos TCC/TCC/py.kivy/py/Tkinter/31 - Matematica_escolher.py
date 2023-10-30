import tkinter as tk
from tkinter import *


janela = tk.Tk()

janela.title("Lear+")
janela.geometry("400x700+100+0")
janela.resizable(False,False)
bg = PhotoImage(file = "py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png") 
label1 = Label( janela, image = bg) 
label1.place(x = -28, y = -15) 


def _init_(self, *args, **kwargs):
    pass

#voltar
photo = PhotoImage(file="py.kivy/py/img_wireframe/voltar.png")
photo = photo.subsample(15, 15)
btn = Button(janela, bd=0, image=photo, text="")
btn.place(x=10, y=10)
txt = Label(janela,text = "Voltar", fg="black", font=('Century Gothic',7))
txt.place(x=12, y=45)

#+ & -
txt1 = Label(janela,text = " + & -", fg="#A020F0", font=('Century Gothic',27))
txt1.place(x=165, y=15)

#upload
photo2 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo2 = photo2.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo2, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=70, y=70,width=115, height=140)

#upload
photo3 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo3 = photo3.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo3, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=70, y=215,width=115, height=140)

# x & /
txt1 = Label(janela,text = "x & /", fg="#A020F0", font=('Century Gothic',27))
txt1.place(x=165, y=355)

#upload
photo4 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo4 = photo4.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo4, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=240, y=410,width=115, height=140)

photo5 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo5 = photo5.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo5, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=240, y=70,width=115, height=140)

photo6 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo6 = photo6.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo6, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=240, y=215,width=115, height=140)

photo7 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo7 = photo7.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo7, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=240, y=410,width=115, height=140)

photo9 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo9 = photo9.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo9, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=240, y=555,width=115, height=140)

#upload
photo0 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo0 = photo0.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                  ", image= photo0, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=70, y=555,width=115, height=140)

#upload
photo11 = PhotoImage(file="py.kivy/py/img_wireframe\ICONS\Matematica\Subir.png")
photo11 = photo11.subsample(17, 17)
btn1 = Button(janela, bd=0,text="                 ", image= photo11, bg="#d3d3d3", compound= RIGHT , font=('Century Gothic',12))
btn1.place(x=70, y=410,width=115, height=140)

janela.mainloop()
Place()