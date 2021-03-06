#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from matrix import *
from node import *

class ID3(object):
	"""docstring for ID3"""
	def __init__(self):
		super(ID3, self).__init__()


	def execute(self, examples, attributes, class_attribute):
		Matrix.print_matrix(examples)
		if len(examples[0]) == 1: # Se examples e vazio (a unica coluna e a do atributo classe )
			majority_value = self.get_majority(examples, class_attribute)
			node = Node(majority_value)
			print("retornando node com label:", majority_value)
			return node # Retorna ocorrencia mais frequente do atributo class
		elif len(Matrix.get_attribute_values(examples, class_attribute)) == 1: # (Se todos os examples tem a mesma classificacao)
			label = list(Matrix.attribute_occurrence_count(examples, class_attribute).keys())[0]
			node = Node(label)
			print("retornando node com label:", label)
			return node # Retorna a classificacao
		elif len(attributes) == 1: # Se atributos e vazio retorna a ocorrencia mais frequente do attributo classe
			majority_value = self.get_majority(examples, class_attribute)
			node = Node(majority_value)
			print("retornando node com label:", majority_value)
			return node
		else:
			best_attribute = self.get_best_attribute(examples, class_attribute, attributes)
			node = Node(attributes[best_attribute])

			if best_attribute < class_attribute:
					class_attribute -= 1

			for key, value in Matrix.attribute_occurrence_count(examples, best_attribute).items():
				print(attributes[best_attribute], "=>", key)
				new_examples = Matrix.remove_line(examples, best_attribute, key)
				columns_to_remove = []
				columns_to_remove.append(best_attribute)
				new_examples = Matrix.remove_columns_2(new_examples, columns_to_remove)

				node.add_children(key, self.execute(new_examples, Matrix.remove_attribute(attributes, best_attribute), class_attribute))
			return node


	def get_best_attribute(self, examples, class_attribute, attributes):
		"""Retorna o indice do atributo com maior ganho de informacao"""
		gains = []
		# Calcula o ganho para cada atributo, exceto o atributo classe
		for attr_index, attribute in enumerate(attributes):
			if attr_index != class_attribute: # Verifica se nao e o atributo classe
				gains.append(self.gain(attr_index, examples, class_attribute))
			else:
				gains.append(-1000)

		return gains.index(max(gains))


	def get_entropy(self, examples, class_attribute):
		"""Retorna a entropia total do conjunto"""
		entropy = 0.0
		total_cases = float(len(examples))

		# Calcula a entropia total dos examples
		for key, occurrence in Matrix.attribute_occurrence_count(examples, class_attribute).items():
			proportion = occurrence / total_cases
			entropy -= proportion * math.log(proportion, 2)

		return entropy


	def get_entropy_per_attribute_value(self, examples, attribute_index, key, total_cases, class_attribute):
		"""
		Retorna a entropia para um valor especifico (aresta) de um determinado atributo.
		Contabilizada de acordo com os valores do atributo classe
		"""
		class_values = Matrix.get_attribute_values(examples, class_attribute)

		# Ocorrencias de um valor do atributo para cada valor do atributo classe
		occurrence_per_attribute_value = {}

		total_cases = float(total_cases)

		for class_value in class_values:
			occurrence_per_attribute_value[class_value] = 0

		# Contabiliza as ocorrencias para cada valor do atributo
		for line in examples:
			if line[attribute_index] == key:
				occurrence_per_attribute_value[line[class_attribute]] += 1

		entropy_per_value = 0.0
		for occurrence_value in occurrence_per_attribute_value.values():
			proportion = occurrence_value / total_cases
			if proportion == 0.0: # log de 0 nao e definido
				return 0.0
			entropy_per_value -= (proportion) * math.log(proportion, 2)

		return entropy_per_value


	def gain(self, attribute_index, examples, class_attribute):
		"""Retorna o ganho de informacao para um determinado atributo"""
		gain = self.get_entropy(examples, class_attribute)
		total_cases = float(len(examples))

		for key, occurrence in Matrix.attribute_occurrence_count(examples, attribute_index).items():
			value_entropy = self.get_entropy_per_attribute_value(examples, attribute_index, key, occurrence, class_attribute)
			gain -= (occurrence / total_cases) * value_entropy

		return gain


	def get_majority(self, examples, class_attribute):
		"""Retorna o valor com maior ocorrencia do atributo classe"""
		class_values = Matrix.attribute_occurrence_count(examples, class_attribute)
		values = list(class_values.values())
		max_index = values.index(max(values))
		return list(class_values.keys())[max_index]
