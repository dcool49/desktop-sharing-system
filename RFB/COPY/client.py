import socket

import pyscreenshot as ImageGrab

if __name__ == "__main__":
     
    ImageGrab.grab_to_file('file.png')
    ImageGrab.grab_to_file('file1.png')
    ImageGrab.grab_to_file('file2.png')
    ImageGrab.grab_to_file('file3.png')
    ImageGrab.grab_to_file('file4.png')

    print "\nImage Caputred"

    host = socket.gethostname()

    port = 5000

    s = socket.socket()

    s.connect((host , port))
        
    f = open("file.png", "rb")
    f1 = open("file1.png", "rb")
    f2 = open("file2.png", "rb")
    f3 = open("file3.png", "rb")
    f4 = open("file4.png", "rb")

    print "\nSending Image File: ", f.name, f1.name, f2.name, f3.name, f4.name

    while True:

        read = f.readline()

        if not read:

            break

        s.send(read)
    read = '01'
    s.send(read)
    f.close()

    while True:

        read = f1.readline()

        if not read:

            break

        s.send(read)
    read = '02'
    s.send(read)
    f1.close()
    while True:

        read = f2.readline()

        if not read:

            break

        s.send(read)
    read = '03'
    s.send(read)
    f2.close()
    while True:

        read = f3.readline()

        if not read:

            break

        s.send(read)
    read = '04'
    s.send(read)
    f3.close()
    while True:

        read = f4.readline()

        if not read:

            break

        s.send(read)
    read = '05'
    s.send(read)
    f4.close()

        
    print "\nImage Send Successfully"
    
    

    s.close()
