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
janela.title("Combobox") # titulo da janela
janela.geometry("300x300") # tamanho da janela


#Nome----------------------
label_nome = Label(janela, width=15, height=2, text='Faça a sua escolha', font=('Arial 12 bold'), fg=cor1, anchor='w')
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


def obter_resultados():
    resultado = combo.get()
    print(resultado)


#criando Combobox
combo = Combobox(janela)

# definindo os valores para combobox
combo["values"] = (1, 2, 3, 4,'Python', 'Tkinter')
combo.current(1)
combo.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)


# Botão --------
botao = Button(janela,command=obter_resultados, width=10, height=1, text='Ver resposta', font=('Arial 12 bold'), relief='solid', fg=cor1)
botao.grid(row=2, column=0, padx=5, pady=20)



janela.mainloop()