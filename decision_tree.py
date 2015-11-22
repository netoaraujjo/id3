#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from node import *
from graphviz import Digraph

class DecisionTree(object):
	global dot

	"""docstring for DecicionTree"""
	def __init__(self, tree):
		super(DecisionTree, self).__init__()
		self.tree = tree
		global dot
		dot = Digraph()
		dot.attr('node', shape='circle')
		self.build_tree(tree)
		dot.view()

	def build_tree(self, node):
		global dot
		if node.get_label() is not None:
			dot.node(node.get_label(), node.get_label())
			if node.get_childrens() is not []:
				childrens = node.get_childrens()
				for child in childrens.keys():
					label = childrens.get(child)
					self.build_tree(childrens.get(child))
					dot.edge(node.get_label(),label.get_label(), label=child)
