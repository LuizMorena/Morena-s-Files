import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd

Cadastro = pd.read_excel('CadastroFilmes.xlsx', engine= 'openpyxl')


lista_genero = ["Ação", "Aventura", "Cinema de Arte", "Chanchada", "Comédia", "Comédia de Ação", "Comédia de Terror",
                "Comédia Dramática", "Comédia Româmtica", "Dança", "Documentário", "Docuficção", "Drama",
                "Espionagem", "Faroeste", "Fantasia", "Fantasia Científíca","Ficção Científica", "Guerra", "Musical",
                "Policial", "Roamnce", "Suspense", "Terror", "Thriller"]
lista_codigos = []

janela = tk.Tk()

#criação da função

def inserir_codigo():
    titulo = entry_titulo.get()
    genero = combobox_selecionar_genero.get()
    diretor = entry_diretor.get()
    ano = entry_ano.get()
    duracao = entry_duracao.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    codigo = Cadastro.shape[0] + len(lista_codigos)+1
    codigo_str = "Cod-{}".format(codigo)
    lista_codigos.append((codigo_str, titulo, genero, diretor, ano, duracao, data_criacao))

#Título da Janela

janela.title('Ferramenta de Cadastro de Filmes')

label_titulo = tk.Label(text="Título do Filme")
label_titulo.grid(row=1, column=0, padx = 10, pady = 10, sticky='nswe', columnspan= 4)

entry_titulo = tk.Entry()
entry_titulo.grid(row=2, column=0, padx=10, pady=10, sticky='nwse', columnspan= 4)

label_genero = tk.Label(text='Gênero')
label_genero.grid(row=3, column=0, padx = 10, pady = 10, sticky='nswe', columnspan= 2)
combobox_selecionar_genero = ttk.Combobox(values=lista_genero)
combobox_selecionar_genero.grid(row=3, column=2, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

label_diretor = tk.Label(text='Diretor')
label_diretor.grid(row=4, column=0, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

entry_diretor = tk.Entry()
entry_diretor.grid(row=4, column=2, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

label_ano = tk.Label(text='Ano')
label_ano.grid(row=5, column=0, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

entry_ano = tk.Entry()
entry_ano.grid(row=5, column=2, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

label_duracao = tk.Label(text='Duração')
label_duracao.grid(row=6, column=0, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

entry_duracao = tk.Entry()
entry_duracao.grid(row=6, column=2, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

botao_criar_codigo = tk.Button(text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(row=7, column=2, padx = 10, pady = 10, sticky='nswe', columnspan= 2)

janela.mainloop()

movo_cadastro = pd.DataFrame(lista_codigos, columns= ["Código", "Título do Filme", "Gênero", "Diretor", "Ano", "Duração", "Data Criação"])
Cadastro = Cadastro.append(movo_cadastro, ignore_index=True)
Cadastro.to_excel('CadastroFilmes.xlsx', index=False)

