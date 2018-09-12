import pyscreenshot as ImageGrab
import time

i=1

if __name__ == "__main__":
    # fullscreen
    
    while i<10:

        ImageGrab.grab_to_file('file%d.png'%(i))
        time.sleep(5)
        i=i+1
        #im=ImageGrab.grab()
        #im.show()



    
