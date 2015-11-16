#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from file_manager import *
from matrix import *
import copy
import id3

def main():
	fm = FileManager()

	file_content = fm.read_csv("/home/neto/weather.csv")

	matrix = copy.deepcopy(file_content)

	Matrix.remove_columns(matrix, [1, 3])

	print("file_content:", id(file_content))
	for f in file_content:
		print(f)

	print("")
	print("matrix:", id(matrix))
	for m in matrix:
		print(m)


if __name__ == '__main__':
	main()