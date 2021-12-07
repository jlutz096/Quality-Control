import cv2 
import numpy as np

#import images
duohex_img = cv2.imread('/home/anx/440/images/2.jpeg', cv2.IMREAD_UNCHANGED)
hexnut_img = cv2.imread('/home/anx/440/images/1.jpeg',cv2.IMREAD_UNCHANGED)


#show images
cv2.imshow('DuoHex', duohex_img)
cv2.imshow('Hex', hexnut_img)
cv2.waitKey()
cv2.destroyAllWindows()

#result
result = cv2.matchTemplate(duohex_img, hexnut_img, cv2.TM_SQDIFF_NORMED) #should be CCOEFF_NORMED

#show result
cv2.imshow("Results",result)
cv2.waitKey()


#gather and print the max_loc and max_val
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_loc, max_val)

#print the min val/loc
print(min_loc, min_val)

#define the w,h
w = hexnut_img.shape[1]
h = hexnut_img.shape[0]

cv2.rectangle(duohex_img, max_loc,(max_loc[0] + w, max_loc[1]+ h), (0,255,255),2)

#threshold
threshold = .5
yloc, xloc = np.where(result >= threshold)

#get
len(xloc)
print(xloc)


#show the result with the threshold
#cv2.imshow('DuoHex with Threshold', duohex_img)
#cv2.waitKey()
#cv2.destroyAllWindows()

#gather rectangles
rectangles = []
for(x,y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

#add weights
rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.5)

for(x,y) in zip(xloc, yloc):
    cv2.rectangle(duohex_img, (x,y), (x+w, y+h), (0,255,255),2)

#display image with weight
cv2.imshow('DuoHex with Weight & Threshold', duohex_img)
cv2.waitKey()
cv2.destroyAllWindows()

