# autocrop
The objective is to crop an image automatically given specific resolution. This can be used to preprocess training images for vision problem. 

# How to run:
1. Install the opencv for python.

> pip install opencv-python

2. Create 3 directories to store the images. 

> masked_image

> unmasked_image

> cropped_image

3. Copy the original images to the unmasked_image directory and masked images to the masked_image directory.

4. Open the crop.py and set the file_num variable with the intended file number, which you want to crop. (For IMG13: just set the value as 13)

5. For other specifications, you can also change the intended height & width, and pixel density. 

6. Run the crop.py

