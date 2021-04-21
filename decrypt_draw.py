#Program: decrypt_draw
#Summary: takes data written by int_convert.py and puts into array of colors. Then draws colors
import os.path
import csv
import pandas as pd
import sys
import random
import numpy
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

#-------------------variables------------------
filename = 'datasrc1.csv'
filenametest = 'test2.txt'
x_max = 200
y_max = 300
window_width_max = 300
window_height_max = 200

#-------------------Copied---------------------

 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Drawn Dots'
        self.left = 10
        self.top = 10
        self.width = window_width_max
        self.height = window_height_max
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
 
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)
        
 
        self.show()
 
 
class PaintWidget(QWidget):
	def paintEvent(self, event):
		qp = QPainter(self)
		pen=qp.pen()
		size = self.size()
		x=-1
		y=-1
		rgbvalIndex = 0

		#call build_rgb_vals()
		rgbvals = build_rgb_vals()

		for j in range(200):
			y+=1
			x=-1
			for i in  range(300):
				x+=1
				try:
					r=rgbvals[rgbvalIndex][0]
					g=rgbvals[rgbvalIndex][1]
					b=rgbvals[rgbvalIndex][2]
					qp.setPen(QColor(r,g,b))
					qp.drawPoint(x, y)
				except IndexError:
					r=rgbvals[rgbvalIndex-1][0]
					g=rgbvals[rgbvalIndex-1][1]
					b=rgbvals[rgbvalIndex-1][2]
					print(str(r)+','+str(g)+','+str(b)+','+str(rgbvalIndex))
					sys.exit()
				
				rgbvalIndex+=1

			


def build_rgb_vals():
	rgbvals = []
	if not os.path.isfile(filename):
		print ('File does not exist.')
		sys.exit()
	else:
		#open filename, read into csv format, remove datetime column
		df = pd.read_csv(filename, header = None)
		del df[0]

		#build list of rgb integer values
		for index, row in df.iterrows():
			for cell in row:
				rgbvals.append(hex_to_rgb(cell))
	return rgbvals

#break up hex value of colors into rgb integer values
def hex_to_rgb(hexcolor):
	wordlist = list(hexcolor)
	r = int((wordlist[0]+wordlist[1]), 16)
	g = int((wordlist[2]+wordlist[3]), 16)
	b = int((wordlist[4]+wordlist[5]), 16)
	rgbvals = [r,g,b]
	return(rgbvals)

#------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


