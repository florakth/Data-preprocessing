# Code reference from Plantcv
# https://plantcv.readthedocs.io/en/latest/installation/
# https://plantcv.readthedocs.io/en/latest/transform_correct_color/

# Flora 2020.9.20

from plantcv import plantcv as pcv
import cv2
import matplotlib. pyplot as plt

# read the images 
target_img, t_path, t_filename = pcv.readimage(filename="./images/undistorted-30-1.jpg")
source_img, s_path, s_filename = pcv.readimage(filename="./images/undistorted-25-1.jpg")

# prepare for getting masks for the two images
dataframe1, start1, space1 = pcv.transform.find_color_card(rgb_img=target_img, background='light')
dataframe2, start2, space2 = pcv.transform.find_color_card(rgb_img=source_img, background='light')

target_mask = pcv.transform.create_color_card_mask(target_img, radius=10, start_coord=start1, 
                                                   spacing=space1, nrows=4, ncols=6)
source_mask = pcv.transform.create_color_card_mask(source_img, radius=10, start_coord=start2, 
                                                   spacing=space2, nrows=4, ncols=6)

# calculate transformation matrix and save it in the current directory
tm, sm, transformation_matrix, corrected_img = pcv.transform.correct_color(target_img=target_img, 
                                                                           target_mask=target_mask, 
                                                                           source_img=source_img, 
                                                                           source_mask=source_mask, 
                                                                           output_directory='.')

print('matrix saved')
# for saving a matrix seperately
#pcv.transform.save_matrix(matrix=transformation_matrix, filename='trans_matrix.npz')


