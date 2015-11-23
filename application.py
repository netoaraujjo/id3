#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import messagebox

from file_manager import *

from matrix import *
import copy
from id3 import *
from decision_tree import *

from PIL import Image, ImageTk


class Application(tk.Frame):
    global counter
    counter = 0
    """docstring for Application"""


    def __init__(self, master=None):
        """Classe que implementa a interface grafica da aplicacao ID3"""

        #Inicializa o Frame
        tk.Frame.__init__(self, master)

        # Modifica o titulo da janela
        master.title('ID3 Algorithm')

        # Seta a organizacao da janela do tipo Grid
        self.grid()

        # Chama a funcao para criar os botoes
        self.create_buttons()


    def open_file(self):
        """Abre um File Dialog que retorna o nome do arquivo e chama a funcao para criar a tabela."""

        global counter

        # Abre o FileDialog e recebe o nome do arquivo escolhido
        filename = filedialog.askopenfilename(**self.file_opt)

        # Verifica se o arquivo vou escolhido
        if filename:
            fm = FileManager()
            # Le os dados de entrada a partir de um arquivo csv
            file_content = fm.read_csv(filename)

            # Clona os dados de entrada
            self.examples = copy.deepcopy(file_content)

            # Remove as colunas fornecidas na lista
            Matrix.remove_columns(self.examples, [0])

            # Obtemos nomes de cada atributo
            self.attributes = Matrix.get_attributes(self.examples)

            # Chama a funcao para criar o combobox
            self.create_combo_box()

            # Chama a funcao para criar a tabela
            self.create_table()

            # Variavel que controla a execucao
            counter = 0


    def create_buttons(self):
        """Funcao que cria os botoes no Frame"""

        # Cria o botao abrir arquivo
        tk.Button(self, text='Abrir arquivo...', command=self.open_file).grid(column = 0, row = 0)

        # Define as opcoes para abrir um arquivo
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Escolha o arquivo de entrada'

        # Cria o botao para remover atributos da tabela
        tk.Button(self, text='Remover Atributo...', command=self.remove_attrib).grid(column = 1, row = 0)

        # Inicializa a combobox como nulo
        self.box = None

        # Cria o botao executar id3
        tk.Button(self, text='Executar ID3...', command=self.execute_id3).grid(column = 3, row = 0)


    def create_combo_box(self):
        """Cria a combobox para a escolha do atributo classe."""
        value = StringVar()
        self.box = ttk.Combobox(self, textvariable=value, state='readonly')
        self.box['values'] = self.attributes
        self.box.current(0)
        self.box.grid(column = 2, row = 0)


    def create_table(self):
        """Funcao que cria a tabela no Frame"""

        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('Atributos', '')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        ysb.grid(row=1, column=3, sticky=tk.N + tk.S)
        xsb.grid(row=2, column=0, sticky=tk.E + tk.W)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Insere cada item dos dados
        for item in self.attributes:
            self.tree.insert('', 'end', values=item)


    def remove_attrib(self):
        """Remover atributo da tabela"""

        if not self.tree.selection():
            #Mensagem de erro gerada quando tentamos remover um atributo sem escolher nenhum
            tk.messagebox.showwarning("Nenhum atributo escolhido", "Escolha um atributo para continuar!")
        elif len(self.attributes) <= 1:
            #Mensagem de erro gerada quando tentamos remover o ultimo atributo
            tk.messagebox.showwarning("Atributo nao pode ser removido", "Numero minimo de atributos atingido!")
        else:
            # Identifica o atributo selecionado para remocao
            checked = (self.tree.selection()[0])[1:]

            # Identifica a posicao do atributo na matriz
            cr = int(checked)-1

            # Remove a coluna fornecidas na lista
            Matrix.remove_columns(self.examples, [cr])

            # Obter os nomes dos atributos restantes
            self.attributes = Matrix.get_attributes(self.examples)

            # Chama a funcao para atualizar o combobox
            self.create_combo_box()

            # Chama a funcao para atualizar a tabela
            self.create_table()


    def execute_id3(self):
        """Funcao que executa o algoritmo id3"""

        global counter

        if self.box is None:
            #Mensagem de erro gerada quando tentamos executar o algoritmo sem antes escolher o arquivo
            tk.messagebox.showwarning("Nenhum arquivo escolhido", "Escolha um arquivo para continuar!")

        elif self.box.get():
            if counter == 0:

                # Colocar o contador em 1 para evitar que o programa execute novamente
                counter = 1

                # Configura o atributo alvo escolhido na combobox
                class_attribute = self.attributes.index(self.box.get())

                # Remove os atributos
                Matrix.extract_attributes(self.examples)

                # Cria instancia da classe ID3
                id3 = ID3()

                # Executa o algoritmo
                tree = id3.execute(self.examples, self.attributes, class_attribute)

                # Cria a arvore de decisao!
                decision_tree = DecisionTree(tree)

                # Carrega a imagem
                imagem = ImageTk.PhotoImage(Image.open("Digraph.gv.png").convert("RGB"))

                # Cria uma nova janela pra exibir a arvore de decisao
                window = tk.Toplevel(self)
                # Cria uma label que ira conter a imagem da arvore de decisao
                label = tk.Label(window, image=imagem)
                label.image = imagem
                label.grid()
            else:
                # Mensagem de erro gerada quando tentamos executar o algoritmo novamente
                tk.messagebox.showwarning("Carregar o arquivo novamente", "Para executar, necessario carregar o arquivo novamente.")
        else:
            # Mensagem de erro gerada quando tentamos executar o algoritmo sem escolher o atributo classe
            tk.messagebox.showwarning("Atributo classe não escolhido", "Escolha o atributo classe para executar!")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
