from calendar import WEDNESDAY
from locale import LC_TIME, setlocale
from tkinter import *
import pyglet
from datetime import datetime


pyglet.font.add_file('digital-7.ttf')

bc = '#ffffff'
fc = '#ff0000'

#configuração da janela
janela = Tk()
janela.title('Relógio digital')
janela.geometry('450x150')
janela.resizable (width=False, height=False)
janela.configure(bg=bc)

def relogio():
    time = datetime.now()
    hora = time.strftime('%H : %M : %S')
    diasemana = time.strftime('%A - ')
    dia = time.day
    mes = time.strftime('%b')
    ano = time.strftime('%Y')
    relogio.configure(text=hora)
    relogio.after(200, clock)
    calendario.configure(text=diasemana + ' ' + str(dia) + '/ ' + 
    str(mes) + '/ ' + str(ano))

relogio = Label(janela, font=('Arial 60'),bg=bc, fg = fc)
relogio.grid(row=0, column=0, padx=5, sticky= NW)

calendario = Label(janela,font=('Arial 20'),bg=bc)
calendario.grid(row=1, column=0, padx=15, sticky=NW)
relogio()


janela.mainloop()

