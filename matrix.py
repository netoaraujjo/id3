#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Matrix:
	"""Classe com operacoes de manipulacao de matrizes"""

	@staticmethod
	def remove_columns(matrix, columns):
		"""Remove as colunas indicadas na lista columns"""
		# new_matrix = []
		columns.reverse()

		for line in matrix:
			for c in columns:
				line.pop(c)

		# for l, line in enumerate(matrix):
		# 	new_line = []
		# 	for c, column in enumerate(line):
		# 		if not c in columns:
		# 			new_line.append(column)
		# 	new_matrix.append(new_line)

		# return matrix
	