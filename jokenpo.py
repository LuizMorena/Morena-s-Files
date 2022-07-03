from random import random
import tkinter
from tkinter import *
from tkinter import ttk

#Importando Pillow
from PIL import Image, ImageTk
import random

from sklearn.decomposition import PCA

# Cores

cor0 = "#FFFFFF"  # branca
cor1 = "#333333"  # preta
cor2 = "#fcc058"  # laranja
cor3 = "#fff873"  # amarela
cor4 = "#34eb3d"   # verde
cor5 = "#e85151"   # vermelha

fundo = "#3b3b3b"

# Configuração da janela
janela = Tk()
janela.title('')
janela.geometry('260x290')
janela.configure(bg=fundo)

# Dividindo a janela em dois frames

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_corpo = Frame(janela, width=260, height=300, bg=cor0, relief='flat')
frame_corpo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Cofigurando o frame de cima

pl_1 = Label(frame_cima, text="Você", height=1, anchor='center',
             font=('Ivy 10 bold'), bg=cor1, fg=cor0)
pl_1.place(x=25, y=70)

pl_1_linha = Label(frame_cima, text="", height=10,
                   anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
pl_1_linha.place(x=0, y=0)


pl_1_pontos = Label(frame_cima, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
pl_1_pontos.place(x=50, y=20)

separador = Label(frame_cima, text=":", height=1,
                  anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
separador.place(x=125, y=20)

pl_2_pontos = Label(frame_cima, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
pl_2_pontos.place(x=170, y=20)

pl_2 = Label(frame_cima, text="PC", height=1, anchor='center',
             font=('Ivy 10 bold'), bg=cor1, fg=cor0)
pl_2.place(x=205, y=70)

pl_2_linha = Label(frame_cima, text="", height=10,
                   anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
pl_2_linha.place(x=255, y=2)

empate = Label(frame_cima, text="", width=255, anchor='center',
               font=('Ivy 10 bold'), bg=cor0, fg=cor0)
empate.place(x=0, y=95)

placar_pc = Label(frame_corpo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
placar_pc.place(x=190,y=10)


global voce
global pc
global rounds
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rounds = 5

#função lógica do jogo
def jogar(i):
    global rounds
    global pontos_voce
    global pontos_pc

    if rounds > 0:
        print(rounds)
        opcoes = ['Pedra','Papel','Tesoura']
        pc = random.choice(opcoes)
        voce = i

        placar_pc['text'] = pc
        placar_pc['fg'] = cor1

        #Caso for igual
        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor3

        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor3

        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor3

        #Outras Possibilidades
        elif voce == 'Pedra' and pc == 'Papel':
            print('PC Ganhou')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor4
            empate['bg'] = cor0

            pontos_pc+=10

        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Você Ganhou')
            pl_1_linha['bg'] = cor4
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor0

            pontos_voce+=10
        
        elif voce == 'Papel' and pc == 'Tesoura':
            print('PC Ganhou')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor4
            empate['bg'] = cor0
            
            pontos_pc+=10

        elif voce == 'Papel' and pc == 'Pedra':
            print('Você Ganhou')
            pl_1_linha['bg'] = cor4
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor0

            pontos_voce+=10

        elif voce == 'Tesoura' and pc == 'Papel':
            print('Você Ganhou')
            pl_1_linha['bg'] = cor4
            pl_2_linha['bg'] = cor0
            empate['bg'] = cor0

            pontos_voce+=10

        elif voce == 'Tesoura' and pc == 'Pedra':
            print('PC Ganhou')
            pl_1_linha['bg'] = cor0
            pl_2_linha['bg'] = cor4
            empate['bg'] = cor0

            pontos_pc+=10

        #atualizando a pontuação
        pl_1_pontos['text'] = pontos_voce
        pl_2_pontos['text'] = pontos_pc

        #Atualizando o número de rounds
        rounds-=1


    else:

        pl_1_pontos['text'] = pontos_voce
        pl_2_pontos['text'] = pontos_pc


        fim_do_jogo()






#Função que inicia o jogo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50),Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_corpo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50),Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_corpo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50),Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_corpo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)




#função terminar o jogo
def fim_do_jogo():
    global rounds
    global pontos_voce
    global pontos_pc

    #Reiniciando as varáveis para 0
    pontos_voce = 0
    pontos_pc = 0
    rounds = 5

    #Eliminando os botões
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    #Definindo o vencedor
    voce_jog = int(pl_1_pontos['text'])
    pc_jog = int(pl_2_pontos['text'])

    if voce_jog > pc_jog:
        placar_vencedor = Label(frame_corpo, text='Parabéns, você ganhou!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
        placar_vencedor.place(x=5,y=60)


    elif voce_jog < pc_jog:
        placar_vencedor = Label(frame_corpo, text='Burrão!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor5)
        placar_vencedor.place(x=5,y=60)
    
    else:
        placar_vencedor = Label(frame_corpo, text='Empate!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
        placar_vencedor.place(x=5,y=60)
        

#jogar de novo
    def jogar_denovo():
        pl_1_pontos['text'] = '0'
        pl_2_pontos['text'] = '0'
        placar_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(frame_corpo, command=jogar_denovo, width=25, text='Jogar de novo', compound=CENTER, bg=fundo, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)
    
 

b_jogar = Button(frame_corpo, command=iniciar_jogo, width=25, text='Jogar', compound=CENTER, bg=fundo, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)














janela.mainloop()
