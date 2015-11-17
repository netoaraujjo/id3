#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from file_manager import *
from matrix import *
import copy
from id3 import *

def main():
	fm = FileManager()

	# Le os dados de entrada a partir de um arquivo csv
	file_content = fm.read_csv("emprestimo.csv")

	# Clona os dados de entrada
	examples = copy.deepcopy(file_content)

	# Remove as colunas fornecidas na lista
	Matrix.remove_columns(examples, [0])

	# Obtemos nomes de cada atributo
	attributes = Matrix.extract_attributes(examples)
	
	# configura o atributo alvo como sendo a ultima coluna (so para testes)
	target = len(examples[0]) - 1

	# Cria instancia da classe ID3
	id3 = ID3(examples, attributes, target)

	# Executa o algoritmo
	id3.execute()
	

if __name__ == '__main__':
	main()