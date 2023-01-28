from tkinter import *
from tkinter import ttk

#Importando as bibliotecas externas -------
from PIL import Image, ImageTk

###############  Cores Usadas ###############
cor0 = "#000000"  # black
cor1 = "#cc1d4e"  # red
cor2 = "#feffff"  # white
cor3 = "#0074eb"  # blue
cor4 = "#435e5a"  # #435e5a
cor5 = "#59b356"  # green
cor6 = "#d9d9d9"  # grey

############# Janelas #############
janela = Tk()
janela.title("") # titulo da janela
janela.geometry("835x360") # tamanho da janela
janela.configure(bg=cor6) # cor do fundo da janela
janela.resizable(False, False)


#### Trabalhando para criar o frame ####

app_name_frame = Frame(janela, width=840, height=50, bg=cor2, relief="flat")
app_name_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

## Mostrando os infectados no frame
mostrar_infect_frame = Frame(janela, width=220, height=100, bg=cor2, relief="flat")
mostrar_infect_frame.grid(row=1, column=0, sticky=NW, padx=5, pady=5)

## Mostrando os recuperados no frame
mostrar_recp_frame = Frame(janela, width=220, height=100, bg=cor2, relief="flat")
mostrar_recp_frame.grid(row=1, column=1, sticky=NW, padx=5, pady=5)

## Mostrando mortes no frame
mostrar_mortes_frame = Frame(janela, width=220, height=100, bg=cor2, relief="flat")
mostrar_mortes_frame.grid(row=1, column=2, sticky=NW, padx=5, pady=5)

## selecinador
select_frame = Frame(janela, width=840, height=50, bg=cor6, relief="flat")
select_frame.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)


#### Criando labels para app_name no frame e imagem  ####

img = Image.open("covid19.png")
img = img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_img = Label(app_name_frame, image=img, width=355, pady=20, anchor=NE, relief="flat", bg=cor2)
app_img.grid(row=0, column=0, pady=5)


app_name = Label(app_name_frame, text="COVID-19", width=20, height=1, pady=20, relief="flat",
            anchor=NW, font=("Helvetica 25 bold"), bg=cor2, fg=cor0)
app_name.grid(row=0, column=1, pady=5)


#### Criando labels para os infectados  ####
label_infect = Label(mostrar_infect_frame, text="Infectados", width=20, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=cor2, fg=cor0)
label_infect.grid(row=0, column=0, pady=1, padx=13)

mostrar_infect = Label(mostrar_infect_frame, text="88373773", width=12, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=cor2, fg=cor0)
mostrar_infect.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_infect_frame, text="Quarta-Feira: 25/01/2023", width=25, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=cor2, fg=cor0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_infect_frame, text="Total casos de ativos de Covid-19", width=33, height=1,padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=cor2, fg=cor0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

barra_azul = Label(mostrar_infect_frame, text="", width=19, height=1, padx=0, pady=1, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=cor3, fg=cor0)
barra_azul.grid(row=4, column=0, pady=1, padx=0, sticky=NSEW)


#### Criando labels para os recuperados  ####
label_recp = Label(mostrar_recp_frame, text="Recuperados", width=20, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=cor2, fg=cor0)
label_recp.grid(row=0, column=0, pady=1, padx=13)

mostrar_recp = Label(mostrar_recp_frame, text="88373773", width=12, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=cor2, fg=cor0)
mostrar_recp.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_recp_frame, text="Quarta-Feira: 25/01/2023", width=25, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=cor2, fg=cor0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_recp_frame, text="Total casos recuperados de Covid-19", width=33, height=1,padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=cor2, fg=cor0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

barra_verde = Label(mostrar_recp_frame, text="", width=19, height=1, padx=0, pady=1, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=cor5, fg=cor0)
barra_verde.grid(row=4, column=0, pady=1, padx=0, sticky=NSEW)

#### Criando labels para os mortes  ####
label_mortes = Label(mostrar_mortes_frame, text="Mortes", width=20, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=cor2, fg=cor0)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(mostrar_mortes_frame, text="88373773", width=12, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=cor2, fg=cor0)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_info_mortes = Label(mostrar_mortes_frame, text="Quarta-Feira: 25/01/2023", width=25, height=1, padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=cor2, fg=cor0)
mostrar_info_mortes.grid(row=2, column=0, pady=1)

mostrar_info_mortes = Label(mostrar_mortes_frame, text="Total casos mortes de Covid-19", width=33, height=1,padx=0, pady=7, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=cor2, fg=cor0)
mostrar_info_mortes.grid(row=3, column=0, pady=1, padx=13)

barra_vermelha = Label(mostrar_mortes_frame, text="", width=19, height=1, padx=0, pady=1, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=cor1, fg=cor0)
barra_vermelha.grid(row=4, column=0, pady=1, padx=0, sticky=NSEW)


################### criando a caixa de seleção ###################

label_pais = Label(select_frame, text="Selecione o país", width=13, height=1,padx=0, pady=7, relief="flat", anchor=NW, font=("Ivy 12 bold"), bg=cor6, fg=cor0)
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Brazil"]

combo = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
combo['values'] =  (pais)
combo.grid(row=0, column=1, padx=0, pady=13)



janela.mainloop()