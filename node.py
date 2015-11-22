#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
	"""docstring for Node"""
	def __init__(self, label):
		self.label = label
		self.childrens = {}


	def add_children(self, edge_label, node):
		self.childrens[edge_label] = node


	def get_childrens(self):
		return self.childrens


	def get_label(self):
		return self.label


	def __str__(self):
		node_str = self.label
		return node_str
