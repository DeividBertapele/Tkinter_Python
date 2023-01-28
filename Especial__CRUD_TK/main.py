from tkinter import *
from tkinter import font, ttk, messagebox

#importando o calendario do Tkinter
from tkcalendar import Calendar, DateEntry

#importando views
from view import *

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


################# Confugrando as janelas ###############
root = Tk()
root.title("")
root.geometry("1043x453")
root.configure(bg=co9)
root.resizable(FALSE,FALSE)


################# Confugrando a janela com frame ###############

#frame cima
frame_cima = Frame(root, width=310, height=50, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0,)

#frame baixo
frame_baixo = Frame(root, width=310, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

#frame direita
frame_direita = Frame(root, width=588, height=403, bg=co1, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0)


################# Confugrando Label cima ###############

app_nome = Label(root, text=" Formulário de Consultoria ", anchor=NW, font=("Ivy 15 bold"), bg=co2, fg=co1, relief="flat")
app_nome.place(x=10, y=10)

#variavel global
global tree

# Função inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    dia = e_cal.get()
    estado = e_est.get()
    sobre = e_sobre.get()
    
    lista = [nome, email, telefone, dia, estado, sobre]
    
    if nome == "":
        messagebox.showerror("Erro", "O nome não pode estar vazio")
    else:
        inserir_info(lista)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")
        e_nome.delete(0, "end")
        e_email.delete(0, "end")
        e_tel.delete(0, "end")
        e_cal.delete(0, "end")
        e_est.delete(0, "end")
        e_sobre.delete(0, "end")

    for widget in frame_direita.winfo_children():
        widget.destroy()
        
    mostrar()   
    
# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = tree_lista[0]
        
        e_nome.delete(0, "end")
        e_email.delete(0, "end")
        e_tel.delete(0, "end")
        e_cal.delete(0, "end")
        e_est.delete(0, "end")
        e_sobre.delete(0, "end")
        
        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_est.insert(0, tree_lista[5])
        e_sobre.insert(0, tree_lista[6])
        
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            dia = e_cal.get()
            estado = e_est.get()
            sobre = e_sobre.get()
            
            lista = [nome, email, telefone, dia, estado, sobre, valor_id]
            
            if nome == "":
                messagebox.showerror("Erro", "O nome não pode estar vazio")
            else:
                atualizar_info(lista)
                messagebox.showinfo("Sucesso", "Os dados foram atualizado com sucesso")
                e_nome.delete(0, "end")
                e_email.delete(0, "end")
                e_tel.delete(0, "end")
                e_cal.delete(0, "end")
                e_est.delete(0, "end")
                e_sobre.delete(0, "end")

            for widget in frame_direita.winfo_children():
                widget.destroy()
                
            mostrar()

        #Botão confirmar para atualização
        b_confirmar = Button(frame_baixo,command=update, text="Confirmar", width=10, anchor=CENTER, font=("Ivy 7 bold"), bg=co2, fg=co1, relief="raised", overrelief="ridge")
        b_confirmar.place(x=116, y=370)
                
    except IndexError:
        messagebox.showerror("Erro", "Seleciona um dos dados na tabela")   
        

#Função deletar        
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = [tree_lista[0]]
        
        deleltar_info(valor_id)
        messagebox.showinfo("Deletado", "Os dados selecinados foram deletados com sucesso")
        
        for widget in frame_direita.winfo_children():
            widget.destroy()
                
        mostrar()
    
    except IndexError:
        messagebox.showerror("Erro", "Seleciona um dos dados na tabela")   
     

################# Confugrando Frame baixo ###############

#Nome
lb_nome = Label(frame_baixo, text="Nome* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_nome.place(x=15, y=40)

#Email
lb_email = Label(frame_baixo, text="Email* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_email.place(x=15, y=100)

#Telefone
lb_tel = Label(frame_baixo, text="Telefone* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_tel.place(x=15, y=160)

#Data da consulta
lb_cal = Label(frame_baixo, text="Data da Consultar* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, bg="darkblue", fg="white", bd=2, year=2023)
e_cal.place(x=15, y=220)

#Estado
lb_est = Label(frame_baixo, text="Estado da Consulta* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_est.place(x=160, y=190)
e_est = Entry(frame_baixo, width=20, justify="left", relief="solid")
e_est.place(x=160, y=220)

#Sobre informações
lb_sobre = Label(frame_baixo, text="informação extra* ", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
lb_sobre.place(x=15, y=260)
e_sobre = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_sobre.place(x=15, y=290)

#Botão inserir
b_inserir = Button(frame_baixo, command=inserir, text="Inserir", width=10, anchor=CENTER, font=("Ivy 9 bold"), bg=co6, fg=co1, relief="raised", overrelief="ridge")
b_inserir.place(x=15, y=340)

#Botão Atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=10, anchor=CENTER, font=("Ivy 9 bold"), bg=co2, fg=co1, relief="raised", overrelief="ridge")
b_atualizar.place(x=112, y=340)

#Botão Deletar
b_deletar = Button(frame_baixo, command=deletar, text="Deletar", width=10, anchor=CENTER, font=("Ivy 9 bold"), bg=co7, fg=co1, relief="raised", overrelief="ridge")
b_deletar.place(x=208, y=340)



################# Confugrando Frame direita  ###############

def mostrar():
    global tree
    
    lista = mostrar_info()

    # lista para cabeçário
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    df_list =  lista

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajusta a coluna 
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()







root.mainloop()
