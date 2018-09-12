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

		def recvall(baglanti, buf):

    			data = ""
    			while len(data) < buf:

        			packet = baglanti.recv(buf - len(data))

        			if not packet:

            				return None

        			data += packet

    			return data


		f = open("image.png", "wb")
		while True:

    			veri = sunucu.recv(512)

    			if not veri:

        			break
    			f.write(veri)
		f.close()

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
