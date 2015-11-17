#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from file_manager import *

class Application(tk.Frame):
	"""
	Application e a classe responsavel pela Interface do ID3
	"""

	def __init__(self, root):

		tk.Frame.__init__(self, root)

		# Define Buttons
		tk.Button(self, text='Abrir arquivo...', command=self.open_file).pack()
		
		# Define as opcoes para abrir um arquivo
		self.file_opt = options = {}
		options['defaultextension'] = '.csv'
		options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
		options['initialdir'] = 'C:\\'
		options['parent'] = root
		options['title'] = 'Escolha o arquivo de entrada'

	def open_file(self):
		"""
		Abre um File Dialog que retorna o nome do arquivo.
		"""
		# get filename
		filename = filedialog.askopenfilename(**self.file_opt)

		# open file on your own
		if filename:
		  	fm = FileManager()

		# Le os dados de entrada a partir de um arquivo csv
		file_content = fm.read_csv(filename)
		print (file_content)

if __name__=='__main__':
	root = tk.Tk()
	Application(root).pack()
	root.mainloop()

