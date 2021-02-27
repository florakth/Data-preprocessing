# Data-preprocessing
Color correction

This work is based on the open source Plantcv

https://plantcv.readthedocs.io/en/latest/installation/
https://plantcv.readthedocs.io/en/latest/transform_correct_color/

Need enviroment :
Install plantcv according to the link above:
For example: conda install plantcv

activate plantv: conda activate plantcv

Conditions: To run color correction on an image, the following are needed: Target and source images must contain a reference from which color values are sampled. 
The following example uses a 24-color Colorchecker passport. A target image (RGB) must be chosen. This image will be of the color profile to which other images 
will be corrected. A source image (RGB), that will be corrected to the target image's color profile A mask (gray-scale) of the target image in which background 
has value 0, and color chips from the colorchecker are labeled with unique values greater than zero, but less than 255. A mask (gray-scale) of the source image 
labeled consistently with the target image's mask.

There are a few important assumptions that must be met in order to automatically detect color cards:

There is only one color card in the image.
Color card should be 4x6 (like an X-Rite ColorChecker Passport Photo). Spacing calculations are based on 4x6 color cards. 
Although starting coordinates will be robust for most color cards, unless an entire row or entire column of chips is missing.
Missing chips may also skew spacing and can also skew starting coordinates.
Color card isn't tilted. The card can be vertical OR horizontal but if it is tilted there will errors in calculating spacing.
