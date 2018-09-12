import subprocess
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def run(self, path):
        subprocess.call(['pythonw',path])
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 370, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda:self.run('server.py'))

        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 301))
        self.label.setText(_fromUtf8(""))
        #self.label.setPixmap(QtGui.QPixmap(_fromUtf8("server.png")))
        #self.label.QPixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("server.png")).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label.setObjectName(_fromUtf8("label"))
        
       
        
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 370, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.fun)
        #self.pushButton_2.clicked.connect(self.label.show)
       # QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.show)
        
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 370, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def fun(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("server.png")).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        #QWidget().resize(QPixmap(_fromUtf8("server.png")).width() , QPixmap(_fromUtf8("server.png")).height())

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SERVER", None))
        self.pushButton.setText(_translate("Dialog", "Capture", None))
        self.pushButton_2.setText(_translate("Dialog", "Refresh", None))
        self.pushButton_3.setText(_translate("Dialog", "Quit", None))



    


if __name__ == "__main__":
    import sys
    import datetime
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())

