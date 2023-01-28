from tkinter import *

#CORES
cor1 = '#f54254' #red
cor2 = '#0000cc' #blue
cor3 = '#000000' #black
cor4 = '#8181a2' #gray
cor5 = '#ffffff' #white

############# Janelas #############
janela = Tk()
janela.title("TESTE DO BOTÃO") # titulo da janela
janela.geometry("500x500") # tamanho da janela
janela.configure(bg=cor5) # cor do fundo da janela

# ---------------------------------------------------#
# # -relief (botão)
# RAISED='raised'
# SUNKEN='sunken'
# FLAT='flat'
# RIDGE='ridge'
# GROOVE='groove'
# SOLID = 'solid'
# ---------------------------------------------------#


############# Botão #############

# botao1 = Button(janela, width=10, height=1, text='Clica Ok!!', font=('Verdana 12 bold'), relief='groove', fg=cor1, bg=cor5)
# botao1.grid(row=6, column=2, padx=5, pady=6)

# botao2 = Button(janela, width=10, height=1, text='Clica Ok!!', font=('Verdana 12 bold'), relief='solid', fg=cor1, bg=cor5)
# botao2.grid(row=7, column=2, padx=5, pady=6)

# botao3 = Button(janela, width=10, height=1, text='Clica Ok!!', font=('Verdana 12 bold'), relief='raised', fg=cor1, bg=cor5)
# botao3.grid(row=8, column=2, padx=5, pady=6)

# botao4 = Button(janela, width=10, height=1, text='Clica Ok!!', font=('Verdana 12 bold'), relief='ridge', fg=cor1, bg=cor5)
# botao4.grid(row=9, column=2, padx=5, pady=6)


## TESTE DO BOTÃO ##

global contador
contador = 0

def executar():
    global contador
    
    text1 = 'Numero impar: '
    text2= 'Numero par: '
    
    if (contador % 2) == 0:
       resultado = text2 + str(contador)
       label['text'] = resultado
       label['fg'] = '#f54254'
       
    else:
        resultado = text1 + str(contador)
        label['text'] = resultado
        label['fg'] = '#000000'
   
    contador += 1
   

label = Label(janela, width=20, height=2, text='Texto será apresentado: ', font=('Arial 12 bold'), relief='flat', fg=cor1, bg=cor5)
label.grid(row=0, column=0, padx=5, pady=10)

botao = Button(janela, command=executar, width=8, height=1, text='Clica Aqui!!', font=('Arial 12 bold'), relief='flat', fg=cor1, bg=cor5)
botao.grid(row=0, column=1, padx=5, pady=10)



janela.mainloop()