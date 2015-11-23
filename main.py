#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from file_manager import *
from matrix import *
import copy
from id3 import *
from decision_tree import *

def main():
	fm = FileManager()

	# Le os dados de entrada a partir de um arquivo csv
	file_content = fm.read_csv("emprestimo.csv")

	# Clona os dados de entrada
	examples = copy.deepcopy(file_content)

	# Remove as colunas fornecidas na lista
	Matrix.remove_columns(examples, [0, 4])

	# Obtemos nomes de cada atributo
	attributes = Matrix.extract_attributes(examples)
	
	# configura o atributo alvo como sendo a ultima coluna (so para testes)
	class_attribute = len(examples[0]) - 1 # indice da coluna do atributo classe
	
	# Matrix.print_matrix(file_content)
	# print("\n",attributes,"\n")
	# Matrix.print_matrix(examples)

	id3 = ID3()
	tree = id3.execute(examples, attributes, class_attribute)

	decision_tree = DecisionTree(tree)

if __name__ == '__main__':
	main()