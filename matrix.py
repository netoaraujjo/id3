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
	def remove_columns_2(matrix, columns):
		"""
		Remove as colunas indicadas na lista columns. 
		A matriz original nao e alterada
		"""
		new_matrix = []
		for line in	matrix:
			new_line = []
			for c, column in enumerate(line):
				if not c in columns:
					new_line.append(column)
			if len(new_line) != 0:
				new_matrix.append(new_line)
		return new_matrix


	def remove_line(matrix, attr_index, attr_value):
		"""
		Remove as linhas com valors da coluna attr_index diferentes de attr_value.
		A matriz original nao e alterada
		"""
		new_matrix = []
		for line in matrix:
			if line[attr_index] == attr_value:
				new_matrix.append(line)
		return new_matrix
		

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
	def remove_attribute(attributes, attr_index):
		"""
		Remove um atributo da lista de atributos.
		A lista original nao e alterada.
		"""
		new_attr = []
		for i, attr in enumerate(attributes):
			if i != attr_index:
				new_attr.append(attr)
		return new_attr


	@staticmethod
	def extract_attributes_2(matrix):
		"""
		Remove a primeira linha, que contem os nomes dos atributos 
		retornando-os na forma de uma lista. A matriz original nao e alterada
		"""
		attributes = matrix[0]
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
		"""Conta o numero de ocorrencias de cada valor em cada atributo"""
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


	@staticmethod
	def attribute_occurrence_count(matrix, attribute_index):
		"""Conta o numero de ocorrencias de cada valor para um determinado atributo em um dicionario"""
		occurrences = {}
		for line in matrix:
			for c, column in enumerate(line):
				if c == attribute_index:
					if column in occurrences.keys():
						occurrences[column] += 1
					else:
						occurrences[column] = 1
		return occurrences


	@staticmethod
	def get_attribute_values(matrix, class_attribute_index):
		"""Retorna os valores possiveis para o attributo classe"""
		values = []
		for line in matrix:
			values.append(line[class_attribute_index])
		return list(set(values))


	@staticmethod
	def print_matrix(matrix):
		"""Imprime uma matriz de bidimensional"""
		print("")
		for line in matrix:
			print(line)
		print("")