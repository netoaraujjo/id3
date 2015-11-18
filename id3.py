#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matrix import *
from node import *
import math

class ID3:
	"""docstring for ID3"""
	
	def __init__(self, examples, attributes, target):
		"""
		Construtor da classe ID3. Configura os parametros iniciais
		"""
		self.occurrences = Matrix.occurrence_count(examples)
		self.total_cases = len(examples)
		self.target = target

		for i in self.occurrences:
			print(i)

		print('\n')

		# Testando Node -----------------------------------------------------
		raiz = Node('MONTANTE')
		childrensRaiz = []

		node1 = Node('SALARIO')
		key1 = {}
		key1['medio'] = node1
		childrensRaiz.append(key1)

		node2 = Node('sim')
		key2 = {}
		node2.setChildrens
		key2['baixo'] = node2
		childrensRaiz.append(key2)

		node3 = Node('CONTA')
		key3 = {}
		key3['alto'] = node3
		childrensRaiz.append(key3)

		raiz.setChildrens(childrensRaiz)

		childrens1 = []

		node4 = Node('nao')
		key4 = {}
		key4['<= 990'] = node4
		childrens1.append(key4)

		node5 = Node('sim')
		key5 = {}
		key5['> 990'] = node5
		childrens1.append(key5)

		node1.setChildrens(childrens1)


		childrens3 = []

		node6 = Node('nao')
		key6 = {}
		key6['nao'] = node6
		childrens3.append(key6)

		node7 = Node('sim')
		key7 = {}
		key7['sim'] = node7
		childrens3.append(key7)

		node3.setChildrens(childrens3)

		print(raiz)


		# for index, at in enumerate(attributes):
		# 	node = Node(at)

		# 	childrens = self.addChildrens(self.occurrences, index)
		# 	node.setChildrens(childrens)

		# 	if index == 1:
		# 		childrens[1]['senior'].setName('test')

		# 	 	node1 = Node()
		# 	 	key = {}
		# 	 	childrensTest = []
		# 	 	key['testArrest'] = node1
		# 	 	childrensTest.append(key)
		# 	 	childrens[1]['senior'].setChildrens(childrensTest)
		# 	 	#print(childrens[1]['senior'])
		# 	 	#print('(' + childrens[1]['senior'] + ')')
				
		# 	print(node)

		# --------------------------------------------------------------------

	

	def execute(self):
		"""Inicia a execucao do algoritmo"""
		self.target_entropy = self.get_entropy(self.target)
		print(self.target_entropy)


	def get_entropy(self, attribute_index):

		entropy = 0.0
		for key, occurrence in self.occurrences[attribute_index].items():
			proportion = float(occurrence) / self.total_cases
			entropy += -(proportion) * math.log(proportion, 2)
		return entropy

	def addChildrens(self, occurrences, attribute_index):
		childrens = []

		for k in occurrences[attribute_index].keys():
			node = Node()
			key = {}
			key[k] = node
			childrens.append(key)

		return childrens