# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:13:51 2021

@author: sabab
"""

import cv2
import glob, os
from PIL import Image
import numpy as np


# filenumber
file_num = 47

# select opacity
alpha = 0.4

# select color code 
color = [0,0,255] # for red color

# search for the original file which specific file_num
file_name = "" 
for file in glob.glob('unmasked_image/*IMG'+str(file_num)+'.png'):
    file_name = file.replace('unmasked_image\\', '')


# read the images 
img_unmasked = cv2.imread(file)
img_masked = cv2.imread(r'''masked_image/IMG'''+str(file_num)+'''.png''')

# select the masked area of the image 
img_masked[np.where((img_masked==[255,255,255]).all(axis=2))] = color

# superimposed image
spimp_img = cv2.addWeighted(img_unmasked,1,img_masked,alpha,0)


# saving the image 
cv2.imwrite('superimposed_image/IMG'+str(file_num)+'.png',spimp_img) 

# for showing images
# img2 = cv2.cvtColor(spimp_img, cv2.COLOR_BGR2RGB)
# im_pil = Image.fromarray(img2)
# im_pil.show()