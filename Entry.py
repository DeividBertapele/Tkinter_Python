from tkinter import *

#CORES
cor1 = '#f54254' #red
cor2 = '#0000cc' #blue
cor3 = '#000000' #black
cor4 = '#8181a2' #gray
cor5 = '#ffffff' #white

############# Janelas #############
janela = Tk()
janela.title("ENTRY") # titulo da janela
janela.geometry("400x280") # tamanho da janela

# Função obter----------------------
def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_resp['text'] = nome
    label_idade_resp['text'] = idade
    label_pais_resp['text'] = pais

    # deletar os dados
    entry_nome.delete(0, "end")
    entry_idade.delete(0, "end")
    entry_pais.delete(0, "end")


    
    

#Nome----------------------
label_nome = Label(janela, width=5, height=2, text='Nome: ', font=('Arial 12 bold'), fg=cor1, anchor='w')
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)
entry_nome = Entry(janela, width=10, font=('Arial 10 bold'))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

#Idade----------------------
label_idade = Label(janela, width=5, height=2, text='Idade: ', font=('Arial 12 bold'), fg=cor1, anchor='w')
label_idade.grid(row=1, column=0,padx=10, pady=5, sticky=NSEW)
entry_idade = Entry(janela, width=10, font=('Arial 10 bold'))
entry_idade.grid(row=1, column=1, padx=10, pady=5)

#País----------------------
label_pais = Label(janela, width=5, height=2, text='País: ', font=('Arial 12 bold'), fg=cor1, anchor='w')
label_pais.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)
entry_pais = Entry(janela, width=10, font=('Arial 10 bold'))
entry_pais.grid(row=2, column=1, padx=10, pady=5)


## Respostas----------------------

label_nome_resp = Label(janela, width=12, height=2, text='', font=('Arial 12 bold'), fg=cor1)
label_nome_resp.grid(row=0, column=2, padx=10, pady=5)

label_idade_resp = Label(janela, width=12, height=2, text='', font=('Arial 12 bold'),  fg=cor1)
label_idade_resp.grid(row=1, column=2,padx=10, pady=5)


label_pais_resp = Label(janela, width=12, height=2, text='', font=('Arial 12 bold'), fg=cor1)
label_pais_resp.grid(row=2, column=2, padx=10, pady=5)


# Botão --------
botao = Button(janela,command=obter, width=8, height=1, text='Ver dados', font=('Arial 12 bold'), relief='solid', fg=cor1)
botao.grid(row=3, column=0, padx=5, pady=20)




janela.mainloop()