#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Tkinter
import Tkconstants
import tkFileDialog
from file_manager import *

class Application(Tkinter.Frame):
	"""Application e a classe responsavel pela Interface do ID3"""

	def __init__(self, root):

		Tkinter.Frame.__init__(self, root)

		# Opcoes para Buttons
		button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

		# Define Buttons
		Tkinter.Button(self, text='Abrir arquivo...', command=self.open_file).pack(**button_opt)
		
		# Define as opcoes para abrir um arquivo
		self.file_opt = options = {}
		options['defaultextension'] = '.csv'
		options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
		options['initialdir'] = 'C:\\'
		options['parent'] = root
		options['title'] = 'This is a title'

	def open_file(self):

		"""
		Abre um File Dialog que retorna o nome do arquivo.
		"""
		# get filename
		filename = tkFileDialog.askopenfilename(**self.file_opt)

		# open file on your own
		if filename:
		  	fm = FileManager()

			# Le os dados de entrada a partir de um arquivo csv
			file_content = fm.read_csv(filename)


if __name__=='__main__':
	root = Tkinter.Tk()
	Application(root).pack()
	root.mainloop()

