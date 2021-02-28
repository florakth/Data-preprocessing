import yaml
import cv2
import numpy as np
import glob
import sys


# K, D come from the result of Calibrationfisheye.py
# if you change the camera or the experiment settings, 
# you need a new yaml file from Calibration.py by using new recorded chessboard images
K=np.array([[356.9902625767917, 0.0, 325.97899759265584],
            [0.0, 354.7472444873411, 238.3739134150395],
            [0.0, 0.0, 1.0]])
D=np.array([[-0.05591803302652892],
            [0.045688072907939456],
            [-0.09907533129077128],
            [0.05759639293858244]])
'''
# Or read K,D from a new yaml file
with open(r'calibration_fisheye_matrix.yaml') as file:
    documents = yaml.full_load(file)
    K = np.asarray(documents['K'])
    D = np.asarray(documents['D'])
'''
DIM=(640, 480)

def undistort(img_path):
   # img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imwrite("undistorted_test.jpg", undistorted_img)
 
   
if __name__ == '__main__':
    #for p in sys.argv[1:]:
    img = cv2.imread('test.jpg')
    undistort(img)
    print('Image saved')

