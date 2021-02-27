# Code reference from Plantcv
# https://plantcv.readthedocs.io/en/latest/installation/
# https://plantcv.readthedocs.io/en/latest/transform_correct_color/

# Flora 2020.9.20

from plantcv import plantcv as pcv
import cv2
import matplotlib. pyplot as plt
import numpy as np

# read the images 
target_img, _, _ = pcv.readimage(filename='./images/undistorted-30-1.jpg')
source_img, _, _ = pcv.readimage(filename='./images/undistorted-25-1.jpg')

with np.load('transformation_matrix.npz') as data:
    transformation_matrix = data['arr_0']

#print(transformation_matrix)

corrected_img = pcv.transform.apply_transformation_matrix(source_img=source_img,
                                                          target_img=target_img,
                                                          transformation_matrix=transformation_matrix)


cv2.imwrite('./images/corrected_img.png', corrected_img)

print('Image saved.')


