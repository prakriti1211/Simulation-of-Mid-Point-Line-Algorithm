import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import array as ar
global x1,y1,x2,y2

# creating a class that inherits the QDialog class
class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mid-Point Line Algorithm Inputs")
        
        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        self.third = QLineEdit(self)
        self.forth = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Initial x-coordinate", self.first)
        layout.addRow("Initial y-coordinate", self.second)
        layout.addRow("Final x-coordinate", self.third)
        layout.addRow("Final y-coordinate", self.forth)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
            return (float(self.first.text()), float(self.second.text()),float(self.third.text()),float(self.forth.text()))


def midPoint(X1 , Y1 , X2 , Y2):
	#function to derive all the points using mid point line algorithm
	#store the initial points in the array 
	a = ar.array('f' , [X1])
	b = ar.array('f' , [Y1])

	#calculate dx & dy
	dx=X2-X1
	dy=Y2-Y1

	# initial value of decision parameter 'd'
	d = dy - (dx/2)
	x = X1
	y = Y1

	# iterate through value of x
	while (x < X2):
		x=x+1
		a.append(x)  #insert the value of next x coordinate in the array
		# E or East is chosen
		if(d < 0):
			d = d + dy
			b.append(y) #insert the value of next y coordinate in the array

		# NE or North East is chosen
		else:
			d = d + (dy - dx)
			y=y+1
			b.append(y) #insert the value of next y coordinate in the array

	print('X-coordinates')
	print(a)
	print('Y-coordinates')
	print(b)
	draw(a,b,X2,Y2) #call the function to plot the points

def draw(a,b,X2,Y2):
	#function to plot the points and draw the lines
        plt.title("Mid Point Line Algorithm")
        plt.ylim(1,Y2+1) #minimum limit of the y aixs
        plt.xlim(1,X2+1) #minimum limit of the x axis
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.ion()
        plt.grid()
        for n in range(len(a)):
            i = a[n]
            j = b[n]
            plt.scatter(i, j)
            plt.pause(0.8)
        plt.ioff()
        plt.draw()
        plt.plot(a,b)
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = InputDialog()
    try:
        if dialog.exec():
           x1,y1,x2,y2=dialog.getInputs()
           midPoint(x1,y1,x2,y2)

    except ValueError:
        error = QMessageBox()
        error.setText("Wrong Input or No Input.")
        error.setWindowTitle("Error")
        error.setIcon(QMessageBox.Warning)
        error.exec_()
       
    exit(0)

    
