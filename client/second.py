import sys
import socket
import pyscreenshot as ImageGrab
from PyQt4 import QtGui, QtCore
import subprocess
import pyhk
import os
import thread
import time
from PIL import Image
'''
def re_req():
    while True:
        host = socket.gethostname()
        port = 5000
        s = socket.socket()
        s.bind((host, port))
        s.listen(1)
        con , address = s.accept()
'''
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def run(self, path):
        subprocess.call(['pythonw',path])

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn1 = QtGui.QPushButton('SEND', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(20, 20)
        btn1.clicked.connect(self.send_img)
        #btn1.clicked.connect(self.close_application)
        btn2 = QtGui.QPushButton('START', self)
        btn2.resize(btn1.sizeHint())
        btn2.move(150, 20)
        btn2.clicked.connect(self.start)
            
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
        hot = pyhk.pyhk()
        id1 = hot.addHotkey(['Ctrl','S'],self.send_img)
        hot.start()

    def close_application(self):
        if __name__ == "__main__":
            host = socket.gethostname()
            port = 5000
            s = socket.socket()

            s.connect((host , port))
            s.send("Akash")

            print "\nConnection Established"

                #s.close()
    def send_img(self):

       if __name__ == "__main__":
           
           ImageGrab.grab_to_file('file.png')
           host = socket.gethostname()
           port = 5000
           s = socket.socket()
           s.bind((host, port))
           s.listen(1)
           con , address = s.accept()

           print "\nImage Caputred"

            
           f = open("file.png", "rb")
           print "\nSending Image File: ", f.name

           while True:

                read = f.readline()

                if not read:
                    break
                con.send(read)
            
           print "\nImage Send Successfully"
            
           f.close()

           s.close()

    def start(self):
            
            #host = "192.168.43.117"
        host=socket.gethostname()
        port = 9000

        i=1
        path = "C:/Users/Akash/Desktop/Mega/working model/New folder/file"
            #directory = os.listdir(path)
            #for file in directory:
        if __name__ == "__main__":
            while True :
                im=ImageGrab.grab_to_file('C:/Users/Akash/Desktop/Mega/working model/New folder/file/image%d.png'%(i))
                time.sleep(1)
                s = socket.socket()
                s.connect((host, port))    
                image='image%d.png'%(i)
                i=i+1
                filename = os.path.join(path, image)
                s.send(image+"\n")
                print(s.recv(1024))
                file_to_send = open(os.path.join(path, image), 'rb')
                s.send(file_to_send.read())
                print('File Sent\n')
                file_to_send.close()
                rec = s.recv(1024)
                print(rec)
                s.close()

            
def communication(threadName,delay):

    def main():
        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


    if __name__ == '__main__':
        main()

def receive_connection(threadName,delay):
    host = socket.gethostname()
    port = 5000
    s = socket.socket()
    s.connect((host , port))
    s.send("yugant12")
    print "\nConnection Established"
    s.close()
    #re_req()
    
        
thread.start_new_thread(communication,("thread 1",1))
thread.start_new_thread(receive_connection,("thread 2",1))

