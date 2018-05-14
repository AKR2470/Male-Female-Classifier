#this is used to convert the images in a folder to the numpy arrays in npy format
#which can be loaded by np.load(filename)

import os
import cv2
import glob
import numpy as np

file_name = 'Final_Dataset.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    changed_dataset = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    changed_dataset = []

i = 0
for img in glob.glob("/home/ankur/Desktop/MFrecog/MFDataset/Male_real_trained/*.jpg"):   #or simply we can use for img in os.listdir("."): and can run the script in particular dir
    image = cv2.imread(img)
    print(np.shape(image))
    print(i)
    i = i+1
    changed_dataset.append([image, 1])
    np.save(file_name, changed_dataset)
