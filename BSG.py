# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:00:30 2019

@author: Vaibhav
"""

from __future__ import print_function, division, absolute_import

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style

import numpy as np
import numpy.core.multiarray
import warnings
import tkinter as tk
from tkinter import ttk
import cv2
from skimage import io
from tkinter import *
from main import *
import main as ff

from pre import *
import pre as pp

style.use('ggplot')
warnings.simplefilter('ignore')

from tkinter import filedialog

global_filename = ""
# ===========================================================================================
def get_input(inp):
    print(inp)

# function to browse files
def browsefunc():
    global global_filename
    filename = filedialog.askopenfilename()
    global_filename = filename
    pathlabel.config(text=filename)

# given the path to image, returns its name
def get_img_name(path):
    path_split = path.split("/")
    return path_split[-1]

# save the genrated image
def save_file(image, img_path, scale):
    img_name = get_img_name(img_path)
    save_img_name = img_name[:-4] + "_SR_x{0}".format(scale) + img_name[-4:]

    save_folder =  filedialog.askdirectory()
    save_file = save_folder + "/" + save_img_name
    
    io.imsave(save_file, image)

# function to Show low resolution image on a new pop up window
def show_lr(path):
    popup_lr = tk.Tk()
    popup_lr.wm_title("Plant Leaf Detection")
    popup_lr.geometry('600x400')
    label = ttk.Label(popup_lr, justify=tk.LEFT, text="""Original  Image""", font=("Verdana", 14, "bold"))
    label.pack(side="top", fill="x", pady=10, padx=10)
    button1 = ttk.Button(popup_lr, text="Preprocessing",command=lambda:  ff.main(global_filename))
    button1.pack(anchor='w',ipadx=10,ipady=10,pady=10,padx=10) 
    
    button2 = ttk.Button(popup_lr, text="Predict      ",command=lambda: pp.final(global_filename))
    button2.pack(anchor='w',ipadx=10,ipady=10,pady=10,padx=10)    
    
    img = io.imread(path)
    if img is None:
        print(path)
        print(type(path))
        print("IMG IS NONE")

    #plt.imshow(img)
    fig, ax = plt.subplots()
    im = ax.imshow(img, origin='upper')
    plt.grid("off")

    canvas = FigureCanvasTkAgg(fig, popup_lr)
    #canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
    label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
    label.pack(side="top", pady=2, padx=30)
    popup_lr.mainloop()
    
# ============================================================================================#
#function to show final image
 
root = tk.Tk()
root.geometry('650x400')
tk.Tk.wm_title(root, "Plant Leaf Detection")
label = ttk.Label(root, text="Plant Leaf Disease Classification", font=("Verdana", 22, "bold"))
label.pack(side="top", pady=30, padx=50)

label = ttk.Label(root, justify=tk.CENTER,
                  text="Click the load button below to select the image file", font=("Verdana", 11))
label.pack(side="top", pady=5, padx=5)

button1 = ttk.Button(root, text="Load Image", command=lambda: browsefunc())
button1.pack(anchor='w',ipadx=10,ipady=10,pady=20,padx=20)


button2 = ttk.Button(root, text="Proceed", command=lambda: show_lr(global_filename))
button2.pack(anchor='w',ipadx=10,ipady=10,pady=20,padx=20)

pathlabel = ttk.Label(root, font=("Verdana", 11, "bold"))
pathlabel.pack(side="top", pady=3, padx=30)

label = ttk.Label(root, justify=tk.CENTER, text="")
label.pack(side="top", pady=1, padx=30)

if __name__== "__main__":
    root.mainloop()
