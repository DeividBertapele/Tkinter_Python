from tkinter import *
from tkinter import ttk

# importando o Pillow
from PIL import Image, ImageTk

from dados import *

#### cores ####
co0 = "#000000"  # Preta
co1 = "#ffffff"  # branca
co2 = "#0000ff"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#eb302d"   # vermelha


# Criando a janela

janela = Tk()
janela.title("Pokedéx")
janela.geometry("550x510")
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")


# Criando frame
frame_pk = Frame(janela, width=550, height=290, relief="flat")
frame_pk.grid(row=1, column=0)

# criando a função para trocar o pokemon
def trocar_pokemon(i):
    global img_pk, pk_img
     
    # trocando a cor do fundo do frame
    frame_pk['bg'] = pokemon[i]['tipo'][3]
     
     
    # tipo do pokemon
    pk_name['text'] = i
    pk_name['bg'] = pokemon[i]['tipo'][3]
    
    pk_tipo['text'] = pokemon[i]['tipo'][1]
    pk_tipo['bg'] = pokemon[i]['tipo'][3]
    
    pk_id["text"] = pokemon[i]['tipo'][0]
    pk_id['bg'] = pokemon[i]['tipo'][3]
    
    img_pk = pokemon[i]["tipo"][2]
    
    # imagem do pokemon
    img_pk = Image.open(img_pk)
    img_pk = img_pk.resize((238, 238))
    img_pk = ImageTk.PhotoImage(img_pk)

    pk_img = Label(frame_pk, image=img_pk, relief="flat", bg=pokemon[i]['tipo'][3], fg=co1)
    pk_img.place(x=60, y=50)

    pk_tipo.lift()

    # Status do pokemon
    pk_hp['text'] = pokemon[i]["status"][0]
    pk_atq['text'] = pokemon[i]["status"][1]
    pk_def['text'] = pokemon[i]["status"][2]
    pk_vel['text'] = pokemon[i]["status"][3]
    pk_total['text'] = pokemon[i]["status"][4]

    # Habilidades do pokemon
    pk_hb1['text'] = pokemon[i]["habilidades"][0]
    pk_hb2['text'] = pokemon[i]["habilidades"][1]


# ---------------------------------------------------------------------------------

# nome
pk_name = Label(frame_pk, text="Pikachu", relief="flat", anchor=CENTER, font=("Fixedsys 20"), bg=co1, fg=co0)
pk_name.place(x=12, y=15)

# Categoria
pk_tipo = Label(frame_pk, text="Elétrico", relief="flat", anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=co1)
pk_tipo.place(x=12, y=50)

# id
pk_id = Label(frame_pk, text="#025", relief="flat", anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=co1)
pk_id.place(x=12, y=75)


# -----> Lado Esquerdo
# Status
pk_status = Label(janela, text="Status", relief="flat", anchor=CENTER, font=("Verdana 20"), bg=co1, fg=co0)
pk_status.place(x=15, y=310)

# HP
pk_hp = Label(janela, text="HP: 100", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pk_hp.place(x=15, y=360)

# Ataque
pk_atq = Label(janela, text="Ataque: 600", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pk_atq.place(x=15, y=385)

# Defesa
pk_def = Label(janela, text="Defesa: 500", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pk_def.place(x=15, y=410)

# Velocity
pk_vel = Label(janela, text="Velocidade: 300", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pk_vel.place(x=15, y=435)

# Total
pk_total = Label(janela, text="Total: 300", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pk_total.place(x=15, y=460)


# -----> Lado direito
# Habilidades
pk_status = Label(janela, text="Habilidades", relief="flat", anchor=CENTER, font=("Verdana 20"), bg=co1, fg=co0)
pk_status.place(x=185, y=310)

# Habilidades01
pk_hb1 = Label(janela, text="Choque de trovão", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co0)
pk_hb1.place(x=195, y=360)

# Habilidades02
pk_hb2 = Label(janela, text="Choque de trovão", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co0)
pk_hb2.place(x=195, y=386)


# Criando os botões para pokemon

# imagem do pokemon1
img_pk1 = Image.open("./images/cabeca-pikachu.png")
img_pk1 = img_pk1.resize((40, 40))
img_pk1 = ImageTk.PhotoImage(img_pk1)

pk_b1 = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=img_pk1, text="Pikachu", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b1.place(x=375, y=10)

# imagem do pokemon2
img_pk2 = Image.open("./images/cabeca-bulbasaur.png")
img_pk2 = img_pk2.resize((40, 40))
img_pk2 = ImageTk.PhotoImage(img_pk2)

pk_b2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=img_pk2, text="Bulbasaur", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b2.place(x=375, y=65)

# imagem do pokemon3
img_pk3 = Image.open("./images/cabeca-charmander.png")
img_pk3 = img_pk3.resize((40, 40))
img_pk3 = ImageTk.PhotoImage(img_pk3)

pk_b3 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=img_pk3, text="Charmander", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b3.place(x=375, y=120)

# imagem do pokemon4
img_pk4 = Image.open("./images/cabeca-dragonite.png")
img_pk4 = img_pk4.resize((40, 40))
img_pk4 = ImageTk.PhotoImage(img_pk4)

pk_b4 = Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=img_pk4, text="Dragonite", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b4.place(x=375, y=175)

# imagem do pokemon5
img_pk5 = Image.open("./images/cabeca-gengar.png")
img_pk5 = img_pk5.resize((40, 40))
img_pk5 = ImageTk.PhotoImage(img_pk5)

pk_b5 = Button(janela, command=lambda:trocar_pokemon('Gengar'), image=img_pk5, text="Gengar", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b5.place(x=375, y=230)

# imagem do pokemon6
img_pk6 = Image.open("./images/cabeca-gyarados.png")
img_pk6 = img_pk6.resize((40, 40))
img_pk6 = ImageTk.PhotoImage(img_pk6)

pk_b6 = Button(janela, command=lambda:trocar_pokemon('Gyarados'),image=img_pk6, text="Gyarados", width=150, relief="flat", overrelief=RIDGE, compound=LEFT,
            anchor=NW, padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0)
pk_b6.place(x=375, y=285)


import random
Lista_pokdemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Dragonite', 'Gengar', 'Gyarados']
pokemon_escolhido = random.sample(Lista_pokdemon, 1)

trocar_pokemon(pokemon_escolhido[0])


janela.mainloop()
