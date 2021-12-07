#imports
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

#get template and compairison image
img = cv2.imread('/home/anx/440/images/duoHex.jpg', 0)
#check if image is opened
assert not isinstance(img,type(None)), 'image not found'

#import second image
img2 = img.copy()
template = cv2.imread('/home/anx/440/images/Hexnut.jpg',0)
w, h = template.shape[::-1]

#create method
methods = ['cv2.TM_CCOEFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    #Apply template matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    #If the method in TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
   # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
   #     top_left = min_loc
   # else:
   #     top_left = max_loc
   # bottom_right = (top_left[0] + w, top_left[1] + h)

   # cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]),plt.yticks([1])
    plt.subplot(122), plt.imshow(img,cmap='gray')
    plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
    plt.suptitle(meth)

    plt.show()


