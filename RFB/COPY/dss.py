import sys
import socket
from PIL import Image
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("dss")
		self.setWindowIcon(QtGui.QIcon())
		self.home()
	def home(self):
		btn = QtGui.QPushButton("connect", self)
		btn.clicked.connect(self.close_application)
		btn.resize(70,40)
		btn.move(100,100)
		self.show()

	def close_application(self):
		host = socket.gethostname()

		port = 5000

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.bind((host, port))

		s.listen(5)

		sunucu , adres = s.accept()

		print("connection is done")

		
		f1 = open("image1.png", "wb")
		f2 = open("image2.png", "wb")
		f3 = open("image3.png", "wb")
		f4 = open("image4.png", "wb")
		f5 = open("image5.png", "wb")
		
		while True:

    			veri = sunucu.recv(512)
    			if veri == '1'
                                break

    			if not veri:

        			break
    			f1.write(veri)
		f1.close()

		while True:

    			veri2 = sunucu.recv(512)
    			if veri2 == "02"
                                break

    			if not veri2:

        			break
    			f2.write(veri2)
		f2.close()

		while True:

    			veri3 = sunucu.recv(512)
    			if veri3 == "03"
                                break

    			if not veri3:

        			break
    			f3.write(veri3)
		f3.close()

		while True:

    			veri4 = sunucu.recv(512)
    			if veri4 == "04"
                                break

    			if not veri4:

        			break
    			f4.write(veri4)
		f4.close()

		while True:

    			veri5 = sunucu.recv(512)
    			if veri5 == "05"
                                break

    			if not veri5:

        			break
    			f5.write(veri5)
		f5.close()





		image = Image.open('image.png')
		image.show()

		print("resim alindi.")


		sunucu.close()

		s.close()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
