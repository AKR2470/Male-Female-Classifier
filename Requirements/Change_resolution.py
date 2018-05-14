# CAution : Only run the script in the desired folder where the images are present

from PIL import Image
import os, sys

path1 = ('/home/ankur/Desktop/MFrecog/MFDataset/Female_train_gray') #from which folder images to
path2 = ('/home/ankur/Desktop/MFrecog/MFDataset/Male_train_changedDPI') #where too save

def resize():
    for item in os.listdir('.'):
        if os.path.isfile(item):
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((64,64), Image.ANTIALIAS)
            imResize.save(str(path2) + f + ' resized.jpg', 'JPEG')

resize()