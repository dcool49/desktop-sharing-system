import sys
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

        btn1 = QtGui.QPushButton('capture', self)


        btn1.resize(btn1.sizeHint())
        btn1.move(20, 20)

        btn1.clicked.connect(lambda:self.run('server.py'))

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 20)

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('SERVER')

        #subprocess.call(['pythonw','3.py'])
        self.show()



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
