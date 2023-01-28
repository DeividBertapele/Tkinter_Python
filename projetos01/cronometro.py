from tkinter import *
import tkinter

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#############  Configurando as janelas #############
janela = Tk()
janela.title("CRONÔMETRO") # titulo da janela
janela.geometry("500x245") # tamanho da janela
janela.configure(bg=cor1) # cor do fundo da janela
janela.resizable(width=False, height=False)


#definindo variáveis globais
global tempo
global rodar
global contador
global limitador


limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5

# função para inicio
def iniciar():
    global tempo
    global contador
    global limitador
    
    if rodar:
        # antes do cronometro começar
        if contador <= -1:
            inicio = 'Começando em ' + str(contador)
            label_tempo["text"] = inicio
            label_tempo["font"] = 'Arial 10'
            
        # Rodando o cronometro  
        else:
            label_tempo["font"] = 'Times 90 bold'
            
            temporario = str(tempo)
            h,m,s = map(int, temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)
            
            if (s >= limitador):
                contador = 0
                m += 1
                
            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)
            
            # Atualizando os valores atuais
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo["text"] = temporario
            tempo = temporario
                  
            
            
        label_tempo.after(1000, iniciar)
        contador += 1


# função para começar
def start():
    global rodar
    rodar = True
    iniciar()
  
    
# função para pausar
def pause():
    global rodar
    rodar = False
    iniciar()


# função para pausar
def restart():
    global contador
    global tempo
    
    # reiniciando o contador
    contador = 0
    
    # reiniciando o tempo
    tempo = "00:00:00"
    label_tempo["text"] = tempo
    

############# Criando labels #############
label_app = Label(janela, text="Cronômetro",font=('Verdade 12 bold'),bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo,font=('Times 90 bold '),bg=cor1, fg=cor6)
label_tempo.place(x=20, y=25)


############# Criando botao #############
botao_start = Button(janela, command=start, text="Start", width=10, height=2, font=('Ivy 12 bold'), relief="raised", overrelief="ridge", bg=cor1, fg=cor2)
botao_start.place(x=40, y=160)

botao_pause = Button(janela,command=pause, text="Pause", width=10, height=2, font=('Ivy 12 bold'), relief="raised", overrelief="ridge", bg=cor1, fg=cor2)
botao_pause.place(x=195, y=160)

botao_restart = Button(janela,command=restart, text="Restart", width=10, height=2, font=('Ivy 12 bold'), relief="raised", overrelief="ridge", bg=cor1, fg=cor2)
botao_restart.place(x=355, y=160)









janela.mainloop()