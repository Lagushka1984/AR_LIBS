import cv2
import os
import numpy as np

path = 'C:/Users/turki/Desktop/ROBOCUP/PYTHON/buffer'

class Robot():
    def __init__(self):
        self.picture = cv2.imread(os.path.join(path , 'picture.jpg'), cv2.IMREAD_GRAYSCALE)

    def SendPicture(self, picture):
        #img = ImageGrab.grab(box)
        #img = cv2.cvtColor(np.array(picture), cv2.COLOR_BGR2GRAY)
        #img.save("picture.jpg")
        cv2.imwrite(os.path.join(path , 'picture.jpg'), picture)
        #cv2.SaveImage(os.path.join(path , 'picture.jpg'), picture)

