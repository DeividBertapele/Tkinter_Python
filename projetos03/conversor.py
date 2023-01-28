from tkinter import *
from tkinter import ttk

#Importando as bibliotecas externas -------
from PIL import Image, ImageTk, ImageDraw, ImageOps

import requests
import json
import string


# Cores -------------------
cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#38576b"  # dark blue / azul escuro


############# Janelas #############
janela = Tk()
janela.title("CONVERSOR") # titulo da janela
janela.geometry("300x320") # tamanho da janela
janela.configure(bg=cor0) # cor do fundo da janela
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use('clam')


############# Criando Frame #############

#dividindo a tela em dois frames ----------
frame_cima = Frame(janela, width=300, height=60, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, columnspan=2)

frame_baixo = Frame(janela, width=300, height=260, bg=cor0, pady=0, padx=5, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#Criando a função converter moeda ----------
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrado = valor.get()
    
    r = requests.get(f"https://v6.exchangerate-api.com/YOUR_API_KEY/latest/{moeda_de}")
    dados = json.loads(r.text)
    cambio = dados["conversion_rates"][moeda_para]

    result = float(valor_entrado) * float(cambio)

    if moeda_para == "USD":
        simbolo = "$"
    elif moeda_para == "EUR":
        simbolo = "€"
    elif moeda_para == "INR":
        simbolo = "₹"
    elif moeda_para == "AOA":
        simbolo = "Kz"
    else:
        simbolo = "R$"
        
    moeda_equivalente = simbolo + "{:,.2f}".format(result)   
  
    app_result['text'] = moeda_equivalente


#Trabalhando no frame Cima ----------
img = Image.open("logo_moeda4.png")
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=5, image=img, compound=LEFT,text="Conversor de Moeda  ", padx=13, pady=30, relief='raised', anchor=CENTER,font=("Arial 16 bold"), bg=cor2, fg=cor0)
app_logo.place(x=0, y=0)



#Trabalhando no frame baixo ----------
app_result = Label(frame_baixo, text="", width=16, height=2, relief='solid', anchor=CENTER, font=("Ivy 15 bold"), bg=cor0, fg=cor1)
app_result.place(x=50, y=10)


moeda = ['AOA', 'BRL', 'EUR', 'INR', 'USD']

app_de = Label(frame_baixo, text="De: ", width=8, height=1, relief='flat', anchor=NW, font=("Ivy 12 bold"), bg=cor0, fg=cor1)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_de.place(x=50, y=115)
combo_de['values'] = (moeda)

app_para = Label(frame_baixo, text="Para: ", width=8, height=1, relief='flat', anchor=NW, font=("Ivy 12 bold"), bg=cor0, fg=cor1)
app_para.place(x=158, y=90)
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_para.place(x=160, y=115)
combo_para['values'] = (moeda)

valor = Entry(frame_baixo, width=22, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)


botao = Button(frame_baixo,command=converter, text="Converter ", width=19, height=1, padx=5, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief="raised", overrelief=RIDGE)
botao.place(x=50, y=210)





janela.mainloop()