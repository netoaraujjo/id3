#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from file_manager import *
from matrix import *
import copy
from id3 import *

class Application(tk.Frame):
    """
    Classe que implementa a interface grafica da aplicacao ID3
    """

    def __init__(self, master=None):

        #Inicializa o Frame
        tk.Frame.__init__(self, master)
        
        # Seta a organizacao da janela do tipo Grid
        self.grid()

        # Chama a funcao para criar os botoes
        self.create_buttons()

    def open_file(self):
        """
        Abre um File Dialog que retorna o nome do arquivo e chama a funcao para criar a tabela.
        """

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

            # Chama a funcao para criar a tabela
            self.create_table()


    def create_buttons(self):
        """
        Funcao que cria os botoes no Frame
        """

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


        # Cria o botao executar id3
        tk.Button(self, text='Executar ID3...', command=self.execute_id3).grid(column = 2, row = 0)


    def create_table(self):
        """
        Funcao que cria a tabela no Frame
        """

        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('Atributos', '')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        ysb.grid(row=1, column=2, sticky=tk.N + tk.S)
        xsb.grid(row=2, column=0, sticky=tk.E + tk.W)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Insere cada item dos dados
        for item in self.attributes:
            self.tree.insert('', 'end', values=item)


    def remove_attrib(self):
        """
        Remover atributo da tabela
        """
        # Identifica o atributo selecionado para remocao
        checked = (self.tree.selection()[0])[1:]

        # Identifica a posicao do atributo na matriz
        cr = int(checked)-1

        # Remove a coluna fornecidas na lista
        Matrix.remove_columns(self.examples, [cr])

        # Obter os nomes dos atributos restantes
        self.attributes = Matrix.get_attributes(self.examples)

        # Chama a funcao para criar a tabela
        self.create_table()



    def execute_id3(self):
        """
        Funcao que executa o algoritmo id3
        """

        # Remove os atributos
        Matrix.extract_attributes(self.examples)

        # configura o atributo alvo como sendo a ultima coluna (so para testes)
        target = len(self.examples[0]) - 1

        # Cria instancia da classe ID3
        id3 = ID3(self.examples, self.attributes, target)

        # Executa o algoritmo
        id3.execute()

        print("Executar!")

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
