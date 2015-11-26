#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
	"""Representa a estrutura de um no da arvore de decisao"""
	def __init__(self, label):
		"""Construtor da classe Node"""
		self.label = label
		self.childrens = {}


	def add_children(self, edge_label, node):
		"""Funcao que adiciona um filho ao no"""
		self.childrens[edge_label] = node


	def get_childrens(self):
		"""Funcao que retorna os filhos do no"""
		return self.childrens


	def get_label(self):
		"""Funcao que retorna o nome do no"""
		return self.label


	def __str__(self):
		"""Retorna uma representacao em string do no"""
		node_str = self.label
		return node_str
