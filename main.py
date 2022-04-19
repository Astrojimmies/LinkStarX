import cv2
import numpy as np
import sys
import io
#open webcam
cam = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cam.isOpened():
    raise IOError("Cannot open webcam")
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 6) // 7, byteorder='big')

while True:
    #read webcam
    ret, frame = cam.read()

    #convert to 1d array
    nu_arra = frame.reshape(-1)
    
    #convert to binary
    bi_arra = np.unpackbits(nu_arra)
    
    #convert to array from binary
    from_bi_arra = np.packbits(bi_arra)
    #convert to 3d array
    nu_pic = from_bi_arra.reshape(480, 640, 3)

    #show feed
    cv2.imshow('frame', nu_pic)

    #close when q key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



#close window and webcam
cam.release()
cv2.destroyAllWindows()



