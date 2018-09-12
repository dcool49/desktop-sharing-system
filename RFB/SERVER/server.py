import socket

from PIL import Image
import LABEL

host = socket.gethostname()

port = 5000

s = socket.socket()

s.bind((host, port))

s.listen(5)

con , address = s.accept()

print "\n Waiting for Image.............."

f = open("server.png", "wb")

while True:

    read = con.recv(1)

    if not read:

        break
    
    f.write(read)
    
f.close()

print "\n Image Received Successfully"

image = Image.open('server.png')

image.show()

con.close()

s.close()
