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

		# Testando Node
		for index, at in enumerate(attributes):
			node = Node(at)
			node.setChildrens(self.addChildrens(self.occurrences, index))
			print(node)
	

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