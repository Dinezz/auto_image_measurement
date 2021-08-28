# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import uuid
import measure_object_size_custom
import os.path
from os import path

# import filedialog module
from tkinter import filedialog
from tkinter import messagebox

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")),
    )

    # Change label contents
    label_file_explorer.configure(text=filename)


def Measure_dim():
    inputfull_path = label_file_explorer["text"]
    if path.exists(inputfull_path):

        parentfolder = os.path.dirname(inputfull_path)
        print("Parent Folder - ", parentfolder)
        print("Selected file - ", inputfull_path)

        # Create a Result Folder
        resultfolder = os.path.join(parentfolder, "Results")
        if not os.path.exists(resultfolder):
            os.makedirs(resultfolder)

        filenamewithext = os.path.basename(inputfull_path)
        print("Input filename -", filenamewithext)

        resultfilename = "Result_" + filenamewithext
        resultfilenamepath = os.path.join(resultfolder, resultfilename)
        print("Result filepath -", resultfilenamepath)
        measure_object_size_custom.Measuredim(inputfull_path, resultfilenamepath)
    else:
        messagebox.showinfo("Info", "No file Selected")


# Create the root window
window = Tk()

# Set window title
window.title("Dimension Measurement - Demo")

# Set window size
window.geometry("350x200")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(
    window,
    text="File Explorer using Tkinter",
    width=50,
    height=4,
    fg="blue",
    wraplength=250,
)


button_explore = Button(window, text="Browse Files", command=browseFiles)

button_measure = Button(window, text="Measure dimension", command=Measure_dim)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.place(x=110, y=100)

button_measure.place(x=90, y=140)

# Let the window wait for any events
window.mainloop()
