from tkinter import Tk, ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

##### cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#Ffffff"  # branca
co2 = "#6f9fbd"  # azul

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

##### Configurando as janelas ------------------------------------
janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.resizable(False, False)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Funçao que retorne as informações
def information():
    city = e_local.get()
    key =  "YOUR KEY API -> " # https://openweathermap.org/api
    api_key = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    #fazendo a chamada da API usando requests
    r = requests.get(api_key)

    #convertendo os dados presente na variável r em dicionário
    dados = r.json()

    print(dados)

    #Obtendo zona , país e horas
    pais_codigo = dados["sys"]["country"]

    #------ zona
    zona_fuso = pytz.country_timezones[pais_codigo]

    #------ pais
    pais = pytz.country_names[pais_codigo]

    #------ Data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

    #------ Horas
    tempo =  dados['main']['temp']
    pressao =  dados['main']['pressure']
    humidade =  dados['main']['humidity']
    velocidade =  dados['wind']['speed']
    descricao =  dados['weather'][0]['description']

    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continent_cod = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_cont_nome = pc.convert_continent_code_to_continent_name(pais_continent_cod)
        
        return pais_cont_nome

    continente = pais_para_continente(pais)


    # passando informações nas Labels
    l_cidade["text"] = city + " - " + pais + " / " + continente
    l_data["text"] = zona_horas
    l_hum["text"] = humidade
    l_hum_sb["text"] = "%"
    l_hum_nome["text"] = "Humidade"
    l_press["text"] = "Pressão: " + str(pressao)
    l_vel["text"] = "Velocidade do Vento: " + str(velocidade)
    l_desc["text"] = descricao
    
    
    # Lógica para trocar o fundo da imagem
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")
    
    global imagem
    
    zona_periodo = int(zona_periodo)
    
    if zona_periodo <= 5:
        # Colocando imagem
        imagem = Image.open("lua.png")
        fundo =  fundo_noite
    elif zona_periodo <= 11:
        imagem = Image.open("sol_dia.png")
        fundo = fundo_dia
    elif zona_periodo <= 19:
        imagem = Image.open("sol_fimtarde.png")
        fundo = fundo_tarde
    elif zona_periodo <= 23:
        imagem = Image.open("lua.png")
        fundo = fundo_noite
    else:
        pass
      
        
    imagem = imagem.resize((120, 120))
    imagem = ImageTk.PhotoImage(imagem)

    l_icon = Label(frame_corpo, image=imagem, bg=fundo, fg=co1)
    l_icon.place(x=190, y=60)
                
                
    # Fundo da imagem
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)
        
    l_cidade["bg"] = fundo
    l_data["bg"] = fundo
    l_hum["bg"] = fundo
    l_hum_sb["bg"] = fundo
    l_hum_nome["bg"] = fundo
    l_press["bg"] = fundo
    l_vel["bg"] = fundo
    l_desc["bg"] = fundo


######  Frames ------------------------------------
frame_top = Frame(janela, width=320, height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)


######  Frames top ------------------------------------
e_local =  Entry(frame_top, width=20, justify="left", font=("", 14), highlightthickness=1, relief="solid")
e_local.place(x=15, y=10)

b_clima =  Button(frame_top,command=information, text="Ver clima",bg=co1, fg=co2, font=("Ivy 9 bold"), relief="raised", overrelief=RIDGE)
b_clima.place(x=250, y=10)


######  Frames corpo ------------------------------------
#cidade
l_cidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 12 bold"))
l_cidade.place(x=10, y=4)

# Data e hora
l_data = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 10 bold"))
l_data.place(x=10, y=54)

#Valor da Humidade
l_hum = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 45"))
l_hum.place(x=10, y=100)

#Simbolo da Humidade
l_hum_sb = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 12 bold"))
l_hum_sb.place(x=85, y=110)

#Nome da Humidade
l_hum_nome = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 10 bold"))
l_hum_nome.place(x=85, y=140)

#Pressão
l_press = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 10 bold"))
l_press.place(x=10, y=184)

#Velocidade
l_vel = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 10 bold"))
l_vel.place(x=10, y=212)


#Descrição
l_desc = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Arial 11 bold"))
l_desc.place(x=190, y=190)



janela.mainloop()