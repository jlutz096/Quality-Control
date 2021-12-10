
#imports for opencv
import cv2
import numpy as np

#from FullQCIM import gradeImage

def gradeImageButton():
    #import images
    #template image
    duohex_img = cv2.imread('/home/anx/440/images/1.jpeg', cv2.IMREAD_UNCHANGED)


    hexnut_img = cv2.imread('/home/anx/440/images/Hexnut.jpg', cv2.IMREAD_UNCHANGED)

    #hexnut_img = cv2.imread('/home/anx/440/images/1.jpeg', cv2.IMREAD_UNCHANGED)
    #show images
    cv2.imshow('Template Image', duohex_img)
    cv2.imshow('Image Being Checked', hexnut_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #results
    result = cv2.matchTemplate(hexnut_img, duohex_img, cv2.TM_CCOEFF_NORMED)

    #show result
    cv2.imshow('Results with TM_CCOEFF_NORMED', result)
    cv2.waitKey()


    #gather and print the max_loc and max_val
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val*100)

    #print the min val and min loc
    print(min_loc, min_val)

    #define the width and height
    w = hexnut_img.shape[1]
    h = hexnut_img.shape[0]

    cv2.rectangle(hexnut_img, max_loc,(max_loc[0] + w, max_loc[1]+ h), (0,255,255),2)

    #ADD threshold
    threshold = .8
    yloc, xloc = np.where(result >= threshold)

    #get and print
    len(xloc)
    print(xloc)

    #gather rectangle
    rectangles = []
    for(x,y) in zip(xloc,yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    #ADD weights
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.9)

    for(x,y) in zip(xloc, yloc):
        cv2.rectangle(hexnut_img, (x,y), (x+w, y+h),(0,255,255),2)

    #display
    cv2.imshow('DuoHex with Weight and Threshold', hexnut_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#import code for window
#file explorer

#import
from tkinter import *

#import file dialog
from tkinter import filedialog

#function for opening window
def browseFiles():
    #should always check home directory
    filename = filedialog.askopenfilename(initialdir="/home/anx/440/images",
    title = "Select a File",
    filetypes = (("Test files",
    "*.txt*"),
    ("all files",
    "*.*")))

    #change labels
    label_file_explorer.configure(text = "File Opened: " + filename)
    return filename



#placeholder for def grade

#create new window
window = Tk()

#set title, size, color
window.title("QCiM")
window.geometry("750x600")
window.config(background = "lightBlue")

#create labels
label_file_explorer = Label(window, text = "Quality Control in Manufacturing (QCiM)", width = 100, height = 4, fg = "blue")

#button explorer
#button_explorer = Button(window, text = "Browse File", command = browseFiles)

#button exit
button_exit = Button(window, text = "Exit", command = exit)

#button grade
button_grade = Button(window, text = "Grade Image", command = gradeImageButton)

#grid method for placements
label_file_explorer.grid(column = 1, row = 1)
#button_explorer.grid(column=1, row = 2)
button_grade.grid(column=1, row = 3)
button_exit.grid(column=1, row =4)

#wait for events
window.mainloop()
