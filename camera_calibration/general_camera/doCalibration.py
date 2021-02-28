import yaml
import cv2
import numpy as np

# if you change the camera or the experiment settings, 
# you need a new yaml file from Calibration.py by using new recorded chessboard images

with open(r'calibration_matrix.yaml') as file:
    documents = yaml.full_load(file)
    mtx = np.asarray(documents['camera_matrix'])
    dist = np.asarray(documents['dist_coeff'])
    #dist = np.array([-0.13615181, 0.53005398, 0, 0, 0])
    print(mtx,dist)
    
img = cv2.imread('.images/1.jpg')
#print(img)
h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
#print(newcameramtx)
#print(roi)

# undistort
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('.images/calibresult-1.png',dst)
