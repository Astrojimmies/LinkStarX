import cv2
import numpy as np
import sys
import io

cam = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cam.isOpened():
    raise IOError("Cannot open webcam")
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 6) // 7, byteorder='big')
while True:
    ret, frame = cam.read()

    bts = bin(frame)

    

    print(bts)

    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break




cam.release()
cv2.destroyAllWindows()



