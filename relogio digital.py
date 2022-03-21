from tkinter import *
import pyglet
import locale
from datetime import datetime
from datetime import date

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

pyglet.font.add_file('ninepin.ttf')
pyglet.font.add_file('digital-7.ttf')

corback = '#fffffe'
corfoot = '#ff000f'

#Configuração de janela
janela = Tk()
janela.title('Relógio digital')
janela.geometry('290x75')
janela.resizable(width=False, height=False)
janela.configure(bg=corback)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H: %M: %S')
    semana = tempo.strftime('%a')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')
    horario.configure(text=hora)
    horario.after(200,relogio)
    data.configure(text=semana + ' - ' + str(dia)+ '/' + str(mes)
    + '/'+ str(ano))
    
horario = Label(janela,text='23:36:00', font=('ninepin 20' or 'Arial 20'), 
    bg=corback,fg=corfoot)
horario.grid(row=0, column=0, padx=10, pady=7, sticky=NW)

data = Label(janela,text='Friday - 18/03/2022', font=('ninepin 12' or 'Arial 12'), bg=corback, fg=corfoot)
data.grid(row=1, column=0,padx=10, sticky=NW)
relogio()
janela.mainloop()

