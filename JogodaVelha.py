import tkinter
from tkinter import *
from tkinter import ttk

# cores ---------------------------------------

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# Criando a janela principal
janela = Tk()
janela.title('')
janela.geometry('260x410')
janela.configure(bg=fundo)

#Dividindo a janela em dois frames

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW,padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

#Configurando o frame de cima

app_1 = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_1.place(x=25, y=10)

app_1 = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_1.place(x=17, y=70)

app_1pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1pontos.place(x=80, y=20)



app_0 = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_0.place(x=170, y=10)

app_0 = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_0.place(x=165, y=70)

app_0pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_0pontos.place(x=130, y=20)


app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)





#Criando a lógica do jogo

jogador_1= "X"
jogador_2= "0"

pontos_1= 0
pontos_2= 0

tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

jogando = 'X'
jogar = ''
placar = 0
rodadas = 0




def iniciar_jogo():
    b_jogar.place(x=800, y=350)
    #Para controlar o jogo
    def controlar(i):
        global jogando
        global placar
        global jogar
       

        #Comparando o valor recebido
        if i == str(1):

            #Verificando se a posição está vazia ou não
            if b_0['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                
                    
        if i == str(2):

            #Verificando se a posição está vazia ou não
            if b_1['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                #Quando o placar for maior ou igual a 5, verificar se há vencedor
                #de acordo com os seguintes padrões

                

        if i == str(3):

            #Verificando se a posição está vazia ou não
            if b_2['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                #Quando o placar for maior ou igual a 5, verificar se há vencedor
                #de acordo com os seguintes padrões

                
                    
        if i == str(4):
             #Verificando se a posição está vazia ou não
            if b_3['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                #Quando o placar for maior ou igual a 5, verificar se há vencedor
                #de acordo com os seguintes padrões

                
            
        if i == str(5):
             #Verificando se a posição está vazia ou não
            if b_4['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                #Quando o placar for maior ou igual a 5, verificar se há vencedor
                #de acordo com os seguintes padrões

                
                    
        if i == str(6):
             #Verificando se a posição está vazia ou não
            if b_5['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                         
        if i == str(7):
             #Verificando se a posição está vazia ou não
            if b_6['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                
        
        if i == str(8):
             #Verificando se a posição está vazia ou não
            if b_7['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

               

        if i == str(9):
             #Verificando se a posição está vazia ou não
            if b_8['text']=='':
                #verificando quem está jogando e definindo a cor do símbolo
                if jogando == 'X':
                    cor=co7
                if jogando == '0':
                    cor=co8
                
                #Definindo a cor do ícone do botão 
                # e marcar aquela posição da tabela com o valor do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                #verificando quem está jogando para poder trocar de jogador
                if jogando == 'X':
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                   jogando = 'X'
                   jogar = 'Jogador 2'
                
                #Somando o placar para a próxima rodada
                placar+=1

                #Quando o placar for maior ou igual a 5, verificar se há vencedor
                #de acordo com os seguintes padrões

        if placar >= 5:
            #linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                        vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                        vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                        vencedor(jogando)
                    
                      #colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                        vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                        vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                        vencedor(jogando)
                    
            #diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                        vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                        vencedor(jogando)
                    
            #empate
            if placar>=9:
                 vencedor('Empate!')
                
    #Decidir o vencedor
    def vencedor(i):
        global tabela
        global pontos_1
        global pontos_2
        global rodadas
        global placar

      

        #bloqueando os botões
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', pady=5, anchor='center', font=('Ivy 13 bold'), bg=co0, fg=co2)
        app_vencedor.place(x=25, y=220)

        if i =="X":
            pontos_2+=1
            app_vencedor['text'] = 'Jogador 2 venceu!'
            app_0pontos['text'] = pontos_2

        if i =="0":
            pontos_1+=1
            app_vencedor['text'] = 'Jogador 1 venceu!'
            app_1pontos['text'] = pontos_1

        if i == 'Foi empate':
            app_vencedor['text'] = 'Foi empate'
        
        def inicio():
            #limpando os botões
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''


            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'

           

            app_vencedor.destroy()
            b_jogar.destroy()

        #Botão Jogar

        b_jogar = Button(frame_baixo, command=inicio, text='Próxima Rodada', width=18, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0)
        b_jogar.place(x=30, y=255)


        def fimdejogo():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if rodadas >= 5:
            fimdejogo()
        else:
            rodadas+=1
             #Reiniciando a tabela
            tabela = [['1','2','3'],['4','5','6'],['7','8','9']]
            placar =0

    #Terminar o jogo
    def terminar():
        global tabela
        global rodadas
        global pontos_1
        global pontos_2
        global placar

        tabela = [['1','2','3'],['4','5','6'],['7','8','9']]
        rodadas = 0
        pontos_1 = 0
        pontos_2 = 0
        placar = 0

        #bloqueando os botões
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_fim = Label(frame_baixo, text='Jogo Encerrado', width=17, relief='flat', pady=5, anchor='center', font=('Ivy 13 bold'), bg=co0, fg=co2)
        app_fim.place(x=25, y=90)

        #Jogar de novo
        def jogar_denovo():
            app_0pontos['text'] = '0'
            app_1pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            #chamando a função iniciar o jogo
            iniciar_jogo()

        b_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar de novo', height=1, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0)
        b_jogar.place(x=70, y=250)


    #Configurando o frame de baixo
    #Linhas Verticais

    app_v = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_v.place(x=90, y=15)

    app_v = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_v.place(x=160, y=15)

    #Linhas Horizontais

    app_h = Label(frame_baixo, text=' ', width=190, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
    app_h.place(x=30, y=83)

    app_h2 = Label(frame_baixo, text=' ', width=190, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
    app_h2.place(x=30, y=150)



    #Linha 0

    b_0 = Button(frame_baixo, command=lambda:controlar('1'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co1)
    b_0.place(x=35, y=25)

    b_1 = Button(frame_baixo, command=lambda:controlar('2'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_1.place(x=102, y=25)

    b_2 = Button(frame_baixo, command=lambda:controlar('3'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_2.place(x=170, y=25)

    #Linha1

    b_3 = Button(frame_baixo, command=lambda:controlar('4'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_3.place(x=35, y=93)

    b_4 = Button(frame_baixo, command=lambda:controlar('5'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_4.place(x=102, y=93)

    b_5 = Button(frame_baixo, command=lambda:controlar('6'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_5.place(x=170, y=93)

    #Linha2

    b_6 = Button(frame_baixo, command=lambda:controlar('7'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_6.place(x=35, y=160)

    b_7 = Button(frame_baixo, command=lambda:controlar('8'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_7.place(x=102, y=160)

    b_8 = Button(frame_baixo, command=lambda:controlar('9'), text='', width=1, relief='flat', font=('Ivy 26 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_8.place(x=170, y=160)

#Botão Jogar

b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0)
b_jogar.place(x=70, y=250)






janela.mainloop()