# CAution : Only run the script in the desired folder where the images are present
import os
import cv2
import numpy as np


path = '/home/ankur/Desktop/MFrecog/MFDataset/Female_dev_gray' #path to the saving folder


i = 0

for img in os.listdir("."):
    image = cv2.imread(img, 0)     #0 => BGR2GRAY conversion
    cv2.imwrite( str(path) + '/Female' + str(i) + ".jpg", image)
    i = i+1



