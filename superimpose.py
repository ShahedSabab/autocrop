# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:13:51 2021

@author: sabab
"""

import cv2
import glob, os
from PIL import Image
import numpy as np


def makeSuperImpose(file_num):
    
    # select opacity
    alpha = 0.4
    
    # select color code 
    color = [0,0,255] # for red color
    
    # search for the original file which specific file_num
    # file_name = "" 
    # for file in glob.glob('unmasked_image/*IMG'+str(file_num)+'.png'):
    #     file_name = file.replace('unmasked_image\\', '')
    
    
    # read the images 
    img_unmasked = cv2.imread(r'''unmasked_image/'''+str(file_num))
    img_masked = cv2.imread(r'''masked_image/'''+str(file_num))
    
    
    # select the masked area of the image 
    img_masked[np.where((img_masked==[255,255,255]).all(axis=2))] = color
    
    # # for showing images
    # img2 = cv2.cvtColor(img_unmasked, cv2.COLOR_BGR2RGB)
    # im_pil = Image.fromarray(img2)
    # im_pil.show()
    
    # # for showing images
    # img2 = cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB)
    # im_pil = Image.fromarray(img2)
    # im_pil.show()
    
    # superimposed image
    spimp_img = cv2.addWeighted(img_unmasked,1,img_masked,alpha,0)
    
    
    # saving the image 
    cv2.imwrite(r'''superimposed_image/'''+str(file_num),spimp_img) 
    
    
    
    
for file_num in glob.glob("masked_image/*.png"):
    file_num = file_num.replace('masked_image\\', '')
    print(file_num)
    makeSuperImpose(file_num)