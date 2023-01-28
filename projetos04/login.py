from tkinter import *
from tkinter import Tk, ttk, messagebox

# cores -----------------------------
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

############# Janelas #############
janela = Tk()
janela.title("Login") # titulo da janela
janela.geometry("310x300") # tamanho da janela
janela.configure(bg=cor1) # cor do fundo da janela
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use('clam')


#Dividindo a janela  ------------------
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief="flat")
frame_cima.grid(row=0, column=0,padx=0, pady=1, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief="flat")
frame_baixo.grid(row=1, column=0,padx=0, pady=1, sticky=NSEW)

#Configurando o frame cima ------------------
l_name = Label(frame_cima, text="LOGIN", anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
l_name.place(x=5, y=5)

l_line = Label(frame_cima, text="", width=275, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
l_line.place(x=10, y=45)

# criando a funçao para entrar no login
credenciais = ['Python', '1234']
def verificar_senha():
    nome = w_name.get()
    senha = w_passw.get()
    
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin')
        
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta')
        
        # deletar itens presentes no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
            
            nova_janela()
            
            
    else:
        messagebox.showwarning('Erro', 'Verifica seu nome e a senha do login..')    

# função após verificação
def nova_janela():
    l_name = Label(frame_cima, text="Usuário: " + credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_name.place(x=5, y=5)

    l_line = Label(frame_cima, text="", width=275, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    l_line.place(x=10, y=45)

    l_name = Label(frame_baixo, text="Seja bem vindo" + credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_name.place(x=5, y=105)




#Configurando o frame baixo ------------------
#Nome
l_name = Label(frame_baixo, text="Nome *", anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
l_name.place(x=10, y=20)
w_name = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid")
w_name.place(x=14, y=50)

# PassWord
l_passw = Label(frame_baixo, text="Password *", anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
l_passw.place(x=10, y=95)
w_passw = Entry(frame_baixo, width=25, justify="left", show="*", font=("", 15), highlightthickness=1, relief="solid")
w_passw.place(x=14, y=130)

# Configurando o botao para confirmar
botao_conf = Button(frame_baixo,command=verificar_senha, text="Entrar", width=38, height=2, bg=cor2, fg=cor1, font=('Ivy 9 bold'), relief="raised", overrelief=RIDGE)
botao_conf.place(x=15, y=180)



janela.mainloop()