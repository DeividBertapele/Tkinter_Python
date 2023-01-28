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
janela.title("RadioButton") # titulo da janela
janela.geometry("300x300") # tamanho da janela

# obtendo os resultados
def obter_resultados():
    resultado = selecionado1.get()
    print(resultado)


selecionado1 = IntVar()
selecionado2 = BooleanVar()
selecionado3 = StringVar()

#criando radiobutton
radio1 = Radiobutton(janela, command=obter_resultados, text="Primeiro", value=1, variable=selecionado1)
radio1.grid(row=1, column=0,padx=5, pady=5, sticky=NSEW)

radio2 = Radiobutton(janela, command=obter_resultados, text="Segundo", value=2, variable=selecionado1)
radio2.grid(row=2, column=0,padx=5, pady=5, sticky=NSEW)

radio3 = Radiobutton(janela, command=obter_resultados, text="Terceiro", value=3, variable=selecionado1)
radio3.grid(row=3, column=0,padx=5, pady=5,  sticky=NSEW)



janela.mainloop()