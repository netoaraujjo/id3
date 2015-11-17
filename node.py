#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
	def __init__(self, name=None):
		"""
		Construtor da classe Node. Configura os parametros iniciais
		"""

		self.name = name
		self.childrens = []


	def setChildrens(self, childrens):
		"""
		Adiciona a lista de filhos de cada Node
		"""

		self.childrens = childrens


	def __str__(self):
		"""
		Retorna um Node em formato de string
		"""

		nodeStr = ""

		nodeStr += self.name + ' | '

		for index in range(len(self.childrens)):
			nodeStr += self.childrens[index].keys()[0]
			if index != len(self.childrens) - 1:
				nodeStr += ' - '

		nodeStr += '\n'
		return nodeStr