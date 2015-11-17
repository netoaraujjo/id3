#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy

class Matrix:
	"""Classe com operacoes de manipulacao de matrizes"""

	@staticmethod
	def remove_columns(matrix, columns):
		"""
		Remove as colunas indicadas na lista columns. 
		A matriz original e alterada
		"""
		columns.reverse()
		for line in matrix:
			for c in columns:
				line.pop(c)
	

	@staticmethod
	def extract_attributes(matrix):
		"""
		Remove a primeira linha, que contem os nomes dos atributos 
		retornando-os na forma de uma lista. A matriz original e alterada
		"""
		attributes = matrix[0]
		matrix.pop(0)
		return attributes

	@staticmethod
	def get_attributes(matrix):
		"""
		Retorna a primeira linha, que contem os nomes dos atributos 
		retornando-os na forma de uma lista. A matriz original nao e alterada
		"""
		attributes = matrix[0]
		return attributes


	@staticmethod
	def occurrence_count(matrix):
		"""Conta o numero de ocorrencias de cada valor em cada coluna"""
		occurrences = []
		mt = numpy.array(matrix).transpose()

		for line in mt:
			occurrence = {}
			for value in line:
				if value in occurrence.keys():
					occurrence[value] += 1
				else:
					occurrence[value] = 1

			occurrences.append(occurrence)
		
		return occurrences