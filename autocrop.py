# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:08:39 2021

@author: sabab
"""

import cv2
import glob, os



def autoCrop(file_num):

    # height and width
    h=512
    w=1024
    
    # if the image is masked then 1 otherwise 0
    mask = 1 
    unmask = 0
    
    # represented in %; how much of the pixels have to be masked 
    mask_threshold = 0.05
    
    # calculate the threshold value for masked pixel
    pixel_threshold = (h*w) * (mask_threshold * 0.01)
    
    # running masked pixel count
    pixel_count = 0
    
    #search for the original file which specific file_num
    # for file in glob.glob('unmasked_image/*IMG'+str(file_num)+'.png'):
    #     file_name = file.replace('unmasked_image\\', '')
    
    
    img_unmasked = cv2.imread(r'''unmasked_image/IMG'''+str(file_num)+'''.png''')
    img_masked = cv2.imread(r'''masked_image/IMG'''+str(file_num)+'''.png''')
    
    # height and width of the image
    height_img = img_masked.shape[0]
    width_img = img_masked.shape[1]
    
    # running image number count
    img_num = 1
    
        
    for x in range(0, width_img, w):
        for y in range(0, height_img, h):
            
            # if the image height becomes greater than the original pixel height
            if(y+h>height_img):
                y -= (y+h)-height_img  
                
            # if the image width becomes greater than the original pixel width
            if(x+w>width_img):
                x -= (x+w)-width_img  
            
            crop_img = img_masked[y:y+h, x:x+w]
            crop_img_un = img_unmasked[y:y+h, x:x+w]
            
            pixel_count = 0
            
            # search for white pixels in the rgb channel 
            for i in range(0, crop_img.shape[0], 1):
                for j in range(0, crop_img.shape[1], 1):
                    
                    # take the rgb pixel value
                    pixel_r = crop_img[i,j][0]
                    pixel_g = crop_img[i,j][1]
                    pixel_b = crop_img[i,j][2]
                    
                    # check if pixel count more than the threshold
                    if(pixel_r == 255 and pixel_g == 255 and pixel_b == 255):
                        pixel_count+=1
                        if(pixel_count > pixel_threshold):
                            break
            
            # cv2.imshow("cropped", crop_img)
            if(pixel_count > pixel_threshold):
                cv2.imwrite("cropped_image/IMG"+str(file_num)+"_00"+str(img_num)+"_"+str(mask)+'.png', crop_img)
                cv2.imwrite("cropped_image/IMG"+str(file_num)+"_00"+str(img_num)+"_"+str(unmask)+'.png', crop_img_un)
                img_num+=1
        
for file_num in glob.glob("masked_image/*.png"):
    file_num = file_num.replace('masked_image\\', '')
    file_num = file_num.strip('.png').strip('IMG')
    print(file_num)
    autoCrop(file_num)
        