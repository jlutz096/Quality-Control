#import Quality control code first
#imports
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

#get template and compairison image
img = cv2.imread('/home/anx/440/images/Hexnut.jpg', 0)
#check if image is opened
assert not isinstance(img,type(None)), 'image not found'

#import second image
img2 = img.copy()
template = cv2.imread('/home/anx/440/images/duoHex.jpg',0)
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

#import code for window
#file explorer

#import
from tkinter import *

#import file dialog
from tkinter import filedialog

#function for opening window

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
    title = "Select a File",
    filetypes = (("Test files",
    "*.txt*"),
    ("all files",
    "*.*")))

    #change labels
    label_file_explorer.configure(text = "File Opened: " + filename)

#placeholder for def grade

#create new window
window = Tk()

#set title, size, color
window.title("QCiM")
window.geometry("750x600")
window.config(background = "white")

#create labels
label_file_explorer = Label(window, text = "File Explorer", width = 100, height = 4, fg = "blue")

#button explorer
button_explorer = Button(window, text = "Browse File", command = browseFiles)

#button exit
button_exit = Button(window, text = "Exit", command = exit)

#button grade
button_grade = Button(window, text = "Grade", command = "tmp")

#grid method for placements
label_file_explorer.grid(column = 1, row = 1)
button_explorer.grid(column=1, row = 2)
button_grade.grid(column=1, row = 3)
button_exit.grid(column=1, row =4)

#wait for events
window.mainloop()
