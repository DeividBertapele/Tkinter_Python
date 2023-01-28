from tkinter import *

#CORES
cor1 = '#f54254' #red
cor2 = '#0000cc' #blue
cor3 = '#000000' #black
cor4 = '#8181a2' #gray
cor5 = '#ffffff' #white

############# Janelas #############
janela = Tk()
janela.title("TESTE") # titulo da janela
janela.geometry("500x500") # tamanho da janela
janela.configure(bg=cor5) # cor do fundo da janela

# colocando icone da janela
janela.iconphoto(False, PhotoImage(file='logo_python.png'))

# redimensionar a janela
janela.resizable(width=True, height=True) 


############# Label e Geometria #############
#Nome
label_nome = Label(janela, width=10, height=2, text='Nome:',font=('Verdana 12 bold'), bg=cor4, fg=cor5)
label_nome.grid(row=0, column=0) # primeira linha
# label_nome.pack(side=RIGHT)
# label_nome.place(x=10, y=10)

nome = Label(janela, width=10, height=2, text='Python',font=('Verdana 12 bold'), bg=cor4, fg=cor5)
nome.grid(row=0, column=1, padx=5, pady=6)
# nome.pack(side=RIGHT)
# nome.place(x=100, y=10)

# Idade
label_idade = Label(janela, width=10, height=2, text='Idade:', font=('Verdana 12 bold'), bg=cor4, fg=cor5)
label_idade.grid(row=1, column=0) # segunda linha
# label_idade.place(x=10, y=60)
# label_idade.pack(side=RIGHT)

idade = Label(janela, width=10, height=2, text='XX', font=('Verdana 12 bold'), bg=cor4, fg=cor5)
idade.grid(row=1, column=1, padx=5, pady=6)
# idade.place(x=100, y=60)
# idade.pack(side=RIGHT)

# País
label_pais = Label(janela, width=10, height=2, text='País:',font=('Verdana 12 bold'), bg=cor4, fg=cor5)
label_pais.grid(row=2, column=0) # terceira linha
# label_pais.place(x=10, y=110)
# label_pais.pack(side=RIGHT)

pais = Label(janela, width=10, height=2, text='Brazil',font=('Verdana 12 bold'), bg=cor4, fg=cor5)
pais.grid(row=2, column=1, padx=5, pady= 6)
# pais.place(x=100, y=110)
# pais.pack(side=RIGHT)


janela.mainloop()