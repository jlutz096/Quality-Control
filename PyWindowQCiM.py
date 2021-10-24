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
