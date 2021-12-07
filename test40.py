import numpy as np
import argparse
import imutils 
import glob
import cv2

#construct argumentparser
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=False, help= "/home/anx/440/images/2.jpeg")
ap.add_argument("-i","--images", required=False,
    help= "/home/anx/440/images")

ap.add_argument("-v","--visualize", 
    help="Flag indicating whether or not to visualize each iteration")

args= vars(ap.parse_args())


#load the image, convert to greyscale, and detect edges
template = cv2.imread('/home/anx/440/images/2.jpeg')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)
cv2.waitKey()

for imagePath in glob.glob(args["images"] + "/*.jpeg"):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None

    for scale in np.linspace(0.2,1.0,20)[::-1]:
        resized = imutils.resize(gray, width= int(gray.shape[1]))
        r = gray.shape[1] / float(resized.shape[1])

    if resized.shape[0] < tH or resized.shape[1] < tW:
        break

#detect edges in resized
edged = cv2.Canny(resized, 50, 200)
result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

#check to see if the iteration should be visualized
if args.get("visualize", False):
    #draw a bounding box 
    clone = np.dstack([edged, edged, edged])
    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
    (maxLoc[0] + tW, maxLoc[1] + tH), (0,0,225),2)
    cv2.imShow("Visualize", clone)
    cv2.waitKey(0)

#if we found a new maximum
if found is None or maxVal > found[0]:
    found = (maxVal, maxLoc, r)

#unpack
(_, maxLoc, r) = found
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

#draw a bounding box
cv2.rectangle(image,(startX, startY), (endX, endY), (0,0,255),2)
cv2.imshow("Image", image)
cv2.waitKey(0)
