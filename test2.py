"""
TODO: As of 11/16/2021 the remaining work to be completed is:
    1. Finish functionality for the connection between Browse File and Grade Image. Browse
    File is when the user selects the file for testing purposes. Grade Image, runs the
    the function gradeImageButton. Grade Image button is the driving code for this project.

    2. Create the dialog that displays the percentage match. When the yellow box is high-
    lighted a percentage should be displayed along side with it. 

    3. Package final product together and share with team. Finish the GitHub repository for
    this project. 

    4. Add more depth to UI. i.e. Color scheme, Name of Window. etc.

    5. Write the Technical Handbook (User Guide) for instructions on accessing and using
    this software.

    Add more depth to UI. i.e. Color scheme, Name of Window. etc.


    ***Outline for Browse File and Grade Image Connections***
    Browse File -> Select Image -> The selected image is loaded into the gradeImageButton
    function -> Grade Image Processes the Image and Returns the Result.

    Browse File -> Select Image -> Load image into function -> Grade Image. 

    Completed Actions as of 11/16/2021 are as follows: 
        1. Main Program is written.
        2. User Interface is complete and all buttons work as intended. No errors are thrown.
        3. Grade Image fuctionality is complete. Remaining work is described above. 
    
    As of current writing, the plan is to have the software user ready by 11/30/2021. This
    way all group members can access and play around with the software, so they can then
    produce a User Manual. 

"""

#imports for opencv
import cv2
import numpy as np

#from FullQCIM import gradeImage

def gradeImageButton():
    #import images
    duohex_img = cv2.imread('/home/anx/440/images/2.jpeg', cv2.IMREAD_UNCHANGED)
    hexnut_img = cv2.imread('/home/anx/440/images/1.jpeg', cv2.IMREAD_UNCHANGED)

    #show images
    cv2.imshow('DuoHex', duohex_img)
    cv2.imshow('HexNut', hexnut_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #results
    result = cv2.matchTemplate(duohex_img, hexnut_img, cv2.TM_CCOEFF_NORMED)

    #show result
    cv2.imshow('Results', result)
    cv2.waitKey()


    #gather and print the max_loc and max_val
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val)

    #print the min val and min loc
    print(min_loc, min_val)

    #define the width and height
    w = hexnut_img.shape[1]
    h = hexnut_img.shape[0]

    cv2.rectangle(duohex_img, max_loc,(max_loc[0] + w, max_loc[1]+ h), (0,255,255),2)

    #ADD threshold
    threshold = .5
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
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.5)

    for(x,y) in zip(xloc, yloc):
        cv2.rectangle(duohex_img, (x,y), (x+w, y+h),(0,255,255),2)

    #display
    cv2.imshow('DuoHex with Weight and Threshold', duohex_img)
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
label_file_explorer = Label(window, text = "File Explorer", width = 100, height = 4, fg = "blue")

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
