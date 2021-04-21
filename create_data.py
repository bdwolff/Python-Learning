#Purpose: To create a 200x300 grid of random RGB values for decrypt_draw to paint
#Summary: Execute a nested for loop in a 200x300 grid and randomize a number inclusively between 0 and 255. Then write to a CSV

import os.path
import csv
import pandas as pd
import sys
import random
import numpy

class RGB:
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

#Array dimensions
ARRAY_LENGTH = 1
ARRAY_HEIGHT = 1

#Create an Array of fixed size
array1 = [ARRAY_LENGTH][ARRAY_HEIGHT]

for j in range(0,ARRAY_LENGTH):
	for i in range(0, ARRAY_HEIGHT):
		red = random.randint(0, 255)
		green = random.randint(0, 255)
		blue = random.randint(0, 255)
		rgb1 = RGB(red, green, blue)
		array1[i][j] = rgb1
		print(rgb1.r, rgb1.g, rgb1.b)