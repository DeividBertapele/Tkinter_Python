from tkinter.ttk import *
from tkinter import *


#CORES
cor1 = '#f54254' #red
cor2 = '#0000cc' #blue
cor3 = '#000000' #black
cor4 = '#8181a2' #gray
cor5 = '#ffffff' #white


############# Janelas #############
janela = Tk()
janela.title("FRAME") # titulo da janela
janela.geometry("400x400") # tamanho da janela


frame1 = Frame(janela, width=200, height=200, bg=cor1)
frame1.grid(row=0, column=0, sticky=NSEW)

frame2 = Frame(janela, width=200, height=200, bg=cor2)
frame2.grid(row=0, column=2, sticky=NSEW)

frame3 = Frame(janela, width=200, height=200, bg=cor3)
frame3.grid(row=1, column=0, sticky=NSEW)

frame4 = Frame(janela, width=200, height=200, bg=cor4)
frame4.grid(row=1, column=2, sticky=NSEW)





janela.mainloop()