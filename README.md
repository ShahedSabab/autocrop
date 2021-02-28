# imagePrep
The objective of this project is to prepare images for the segmentation tasks. This can be used as an immediate image pre-processing step for vision models such as [https://www.researchgate.net/publication/336358391_SDDNet_Real-time_Crack_Segmentation]: SDD-Net  and [https://arxiv.org/abs/1505.04597]: U-Net. There are different pre-processing scripts avaialble in this repo. They are the followings:

• autocop.py: This can be used to crop a larger image into smaller portions given dimensions, and pixel density.

• superimpose.py: This can be used to superimpose 2 different images.

• gimp2pngconversion.py: This can be used to convert a .xcf file to png. 

# How to run:
To run the autocrop.py please see the following instructions: 
```
1. Install the opencv for python.
> pip install opencv-python

2. Create 3 directories to store the training images. 
> masked_image
> unmasked_image
> cropped_image

3. Copy the original images to the unmasked_image directory and masked images to the masked_image directory.

4. Open the crop.py and set the file_num variable with the intended file number, which you want to crop. (For IMG13: just set the value as 13)

5. For other modifications, you can also change the intended height & width, and pixel density. 

6. Run the crop.py

7. Check the cropped_image directory for the cropped images.
```
