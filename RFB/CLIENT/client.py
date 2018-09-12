import socket

import pyscreenshot as ImageGrab

if __name__ == "__main__":
     
    ImageGrab.grab_to_file('file.png')

    print "\nImage Caputred"

    host = socket.gethostname()

    port = 5000

    s = socket.socket()

    s.connect((host , port))
        
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
