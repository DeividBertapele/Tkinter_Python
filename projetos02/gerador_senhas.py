from tkinter import *
from tkinter import ttk, messagebox

# Importando Pillow
from PIL import Image, ImageTk

# Importando strings
import string
import random


# Cores -------------------
cor0 = "#444466" # Black / Preto
cor1 = "#feffff" # White / Branco
cor3 = "#f05a43" # Red / Vermelho


############# Janelas #############
janela = Tk()
janela.title("Gerenciador de Senhas") # titulo da janela
janela.geometry("295x360") # tamanho da janela
janela.configure(bg=cor1) # cor do fundo da janela


estilo = ttk.Style(janela)
estilo.theme_use('clam')


############# Criando Frame #############

#dividindo a tela em dois frames ----------
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#Trabalhando no frame Cima ----------
img = Image.open("password02.png")
img = img.resize((35, 35), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)

app_name = Label(frame_cima,text="GERADOR DE SENHAS",font=('Ivy 15 bold'), width=20, height=1, padx=0, relief='flat',anchor='center', bg=cor1, fg=cor0)
app_name.place(x=35, y=3)

app_line = Label(frame_cima,text="",font=('Ivy 1'), width=295, height=0, padx=0, relief='flat',anchor='nw', bg=cor3, fg=cor0)
app_line.place(x=0, y=37)


#Função para gerar senha ----------
def gerar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*/\|'
    
  
    global combinar
    
    # Condição para maiuscula
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass  

    # Condição para minuscula
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass  

    # Condição para numeros
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass  

    # Condição para simbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass  
    
    
    comp = int(spin.get())
    senha = "".join(random.sample(combinar, comp))
   
    app_senha['text'] = senha

    def copiar():
        info =  senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "Senha foi copiada com sucesso")
    bot_copy = Button(frame_baixo,command=copiar, text="Copiar", width=7, height=2, relief="raised", overrelief="solid", anchor="center", font=("Ivy 10 bold"), bg=cor1, fg=cor0)
    bot_copy.grid(row=0, column=1, sticky=NW, padx=5, pady=7, columnspan=1)


#Trabalhando no frame Baixo ----------
app_senha = Label(frame_baixo,text="",font=('Ivy 12 bold'), width=20, height=2,padx=0, relief='solid',anchor='center', bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo,text="Numero total de caracteres na senha",font=('Ivy 10 bold'), height=1, padx=0, relief='flat',anchor='nw', bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=3, pady=1)


var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=2, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)


alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*/\|'


frame_carct = Frame(frame_baixo, width=280, height=210, bg=cor1, pady=0, padx=0, relief='flat')
frame_carct.grid(row=3, column=0, sticky=NSEW, columnspan=3)


#Trabalhando Letras maiúsculas ----------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_carct, width=1, var=estado_1, onvalue=alfa_maior, offvalue="off", relief="flat", bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_carct,text="ABC Letras maiúsculas",font=('Ivy 10 bold'), height=1, padx=0, relief='flat',anchor='nw', bg=cor1, fg=cor0)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)


#Trabalhando Letras minúsculas ----------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_carct, width=1, var=estado_2, onvalue=alfa_menor, offvalue="off", relief="flat", bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_carct,text="abc Letras minúsculas",font=('Ivy 10 bold'), height=1, padx=0, relief='flat',anchor='nw', bg=cor1, fg=cor0)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)


#Trabalhando com Numeros ----------
estado_3 = IntVar()
estado_3.set(False)
check_3 = Checkbutton(frame_carct, width=1, var=estado_3, onvalue=numeros, offvalue="off", relief="flat", bg=cor1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_carct,text="Numeros 123456789",font=('Ivy 10 bold'), height=1, padx=0, relief='flat',anchor='nw', bg=cor1, fg=cor0)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)


#Trabalhando com Simbolos ----------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_carct, width=1, var=estado_4, onvalue=simbolos, offvalue="off", relief="flat", bg=cor1)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_carct,text="Simbolos []{}()*/\|",font=('Ivy 10 bold'), height=1, padx=0, relief='flat',anchor='nw', bg=cor1, fg=cor0)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)


#Trabalhando com Botão ----------
bot_senha = Button(frame_carct, command=gerar_senha, text="Gerar Senha", width=34, height=1, relief="flat", overrelief="solid", anchor="center", font=("Ivy 10 bold"), bg=cor3, fg=cor1)
bot_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)

bot_copy = Button(frame_baixo,text="Copiar", width=7, height=2, relief="raised", overrelief="solid", anchor="center", font=("Ivy 10 bold"), bg=cor1, fg=cor0)
bot_copy.grid(row=0, column=1, sticky=NW, padx=5, pady=7, columnspan=1)






janela.mainloop()




