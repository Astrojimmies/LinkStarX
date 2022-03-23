from asyncore import write
from email.mime import image
from tkinter import Frame
import cv2
from cv2 import CAP_CMU1394
import numpy as np
import sys
import io

cam = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cam.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cam.read()

    _, bts = cv2.imencode('.webp', frame)
    string_pic = str(bts)

    cool_stuff = ' '.join(format(x, 'b') for x in bytearray(string_pic, 'utf-8'))
    print(cool_stuff)
    
    buff = np.fromstring(cool_stuff, np.uint8)
    buff = buff.reshape(1, -1)
    img = cv2.imdecode(buff, cv2.IMREAD_COLOR)


    cv2.imshow('Input', img)

    c = cv2.waitKey(1)
    if c == 27:
        break

cam.release()
cv2.destroyAllWindows()



