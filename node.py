#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
	def __init__(self, name=None):
		"""
		Construtor da classe Node. Configura os parametros iniciais
		"""

		self.name = name
		self.childrens = []	# Lista de dicionarios contendo [{'aresta', No}]


	def setChildrens(self, childrens):
		"""
		Adiciona a lista de filhos de cada Node
		"""
		self.childrens = childrens

	def getChildrens(self):
		return self.childrens

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def __str__(self):
		"""
		Retorna um Node em formato de string
		"""

		nodeStr = ""
		space = "  "

		nodeStr += self.name + '\n'

		for index in range(len(self.childrens)):
			nodeStr += space + '|_ (' + self.childrens[index].keys()[0] + ') '
			nodeStr += self.strAux(self.childrens[index].values()[0], (space + "  "))

		nodeStr += '\n'
		return nodeStr


	def strAux(self, node, spaceAux):
		"""
		
		"""
		strReturn = ""

		if node.getName() is not None:
			strReturn += node.getName() + '\n'
			for i in range(len(node.getChildrens())):
				strReturn += spaceAux + '|_ (' + node.getChildrens()[i].keys()[0] + ') '
				if node.getChildrens()[i].values()[0] is not []:
					strReturn += self.strAux(node.getChildrens()[i].values()[0], (spaceAux + "  "))


		return strReturn
