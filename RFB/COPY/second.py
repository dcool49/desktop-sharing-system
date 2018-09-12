import sys
import socket
import pyscreenshot as ImageGrab
from PyQt4 import QtGui, QtCore
import subprocess

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()


    def run(self, path):
        subprocess.call(['pythonw',path])

 
    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        #btn1 = QtGui.QPushButton('CONNECT', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(20, 20)
        btn1.clicked.connect(self.close_application)

        btn2 = QtGui.QPushButton('START', self)
        btn2.resize(btn1.sizeHint())
        btn2.move(150, 20)
        btn2.clicked.connect(self.send_img)

        btn3 = QtGui.QPushButton('STOP', self)
        btn3.resize(btn1.sizeHint())
        btn3.move(300, 20)
        #btn1.clicked.connect(lambda:self.run('client.py'))

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(400, 20)

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('CLIENT')

        #subprocess.call(['pythonw','3.py'])
        self.show()

    def close_application(self):


        if __name__ == "__main__":
            
            host = socket.gethostname()

            port = 5000

            s = socket.socket()

            s.connect((host , port))

            print "\nConnection Established"

            #s.close()

    def send_img(self):

        if __name__ == "__main__":
            
            host = socket.gethostname()

            port = 5000

            s = socket.socket()

            s.connect((host , port))


            ImageGrab.grab_to_file('file.png')

            print "\nImage Caputred"

        
            f = open("file.png", "rb")

            print "\nSending Image File: ", f.name

            while True:

                read = f.readline()

                if not read:

                    break

                s.send(read)
        
            print "\nImage Send Successfully"
    
            f.close()

            s.close()




def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
