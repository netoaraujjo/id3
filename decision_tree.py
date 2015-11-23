#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from node import *
from graphviz import Digraph

class DecisionTree(object):
	"""docstring for DecisionTree"""
	global dot

	def __init__(self, tree):
		"""Construtor da classe DecisionTree"""

		super(DecisionTree, self).__init__()

		self.tree = tree

		global dot
		dot = Digraph(format='png')
		dot.attr('node', shape='circle')

		# Contador do node
		counter = 0

		# Chama o metodo de criacao da arvore de decisao
		self.build_tree(tree, counter)

		# Renderiza a arvore de decisao
		dot.render(view=False, cleanup=False)


	def build_tree(self, node, counter):
		"""Metodo que percorre os nos e retorna a representacao grafica da arvore de decisao"""

		global dot

		# Verifica se o no e nulo
		if node.get_label() is not None:
			# Cria o no na interface
			father_label = node.get_label() + str(counter)
			counter += 1
			dot.node(father_label, node.get_label())
			# Verifica se o no tem filhos
			if node.get_childrens() is not []:
				# Cria uma lista de filhos
				childrens = node.get_childrens()
				#Percorre o dicionario de filhos
				for child in childrens.keys():
					# Cria um no filho
					child_label = childrens.get(child)
					# Chama o metodo pra criar a arvore de decisao com o no filho
					self.build_tree(childrens.get(child), counter)
					# Cria a ligacao entre o no pai e o no filho na interface
					dot.edge(father_label, child_label.get_label()+str(counter), label=child)
