# Data-preprocessing

This work includes two parts: Camera calibration and color correction, which belongs to RPL department at KTH.

1. Camera calibration

References:
https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html
https://docs.opencv.org/3.4/db/d58/group__calib3d__fisheye.html
https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0

Enviroment: OpenCV, Python3, Numpy

Camera calibration inludes two situations: genral webcamera and fisheye camera
For each one, we need recording chessboard images with different positions and different views, please refer to the images folder.

To get matrix from the chessboard images: 
Calibration.py or Calibrationfisheye.py

To do calibarion with the matrix:
DoCalibration.py or DoCalibrationfisheye.py

2. Color correction

This work is based on the open source Plantcv and OpenCV 

https://plantcv.readthedocs.io/en/latest/installation/
https://plantcv.readthedocs.io/en/latest/transform_correct_color/

Need enviroment :
Install plantcv according to the link above:

For example: conda install plantcv

Activate plantv: 

conda activate plantcv

To run color correction on an image, the following are needed: 

Target and source images must contain a reference from which color values are sampled. 
The following example uses a 24-color Colorchecker passport. A target image (RGB) must be chosen.
This image will be of the color profile to which other images will be corrected. 
A source image (RGB), that will be corrected to the target image's color profile 
A mask (gray-scale) of the target image in which background has value 0, 
and color chips from the colorchecker are labeled with unique values greater than zero, 
but less than 255. A mask (gray-scale) of the source image labeled consistently with the target image's mask.

There are a few important assumptions that must be met in order to automatically detect color cards:

There is only one color card in the image.
Color card should be 4x6 (like an X-Rite ColorChecker Passport Photo). Spacing calculations are based on 4x6 color cards. 
Although starting coordinates will be robust for most color cards, unless an entire row or entire column of chips is missing.
Missing chips may also skew spacing and can also skew starting coordinates.
Color card isn't tilted. The card can be vertical OR horizontal but if it is tilted there will errors in calculating spacing.

For experiment and check the details:

color_correction.ipynb

For color correction work:
1.  Getting the trasformation matrix based on the curret source image and target image:

get_tranform_matrix.py

2.  For a new image, apply this trasform matrix to it to get the corrected image:

apply_transform.py
