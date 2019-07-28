import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
from keras.optimizers import Adam
from sklearn.preprocessing import LabelBinarizer
from keras.models import model_from_json
from keras.models import load_model
from keras import backend as K
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

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


def final(ab):
    popup_lr = tk.Tk()
    popup_lr.wm_title("Last Image")
    label = ttk.Label(popup_lr, justify=tk.LEFT, text="""Detected Disease""", font=("Verdana", 14, "bold"))
    label.pack(side="top", fill="x", pady=10, padx=10)

    lb = pickle.load(open(f"label_transform.pkl","rb"))
    
    saved_classifier_model = pickle.load(open(f"cnn_model_gpu.pkl",'rb'))
    
    EPOCHS = 50
    INIT_LR = 1e-3
    opt=Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    saved_classifier_model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    
    default_image_size = tuple((256, 256))
    image = cv2.imread(ab)
    image = cv2.resize(image, (256,256))
    image = img_to_array(image)
    img = np.reshape(image,[1,256,256,3])
    pre=saved_classifier_model.predict_classes(img)
    print("ABC-->",pre)
    pre=saved_classifier_model.predict(img,batch_size=32)
    print(pre[0])
    
    disease = f"{lb.inverse_transform(pre)[0]}"
    print("The Disease detected is :",disease)
    
##--------------------------GUI----------------------##    
    
    if disease=='Peach___Bacterial_spot':
        img = io.imread(ab)
        label = ttk.Label(popup_lr, justify=tk.CENTER,
                  text="Peach___Bacterial_spot", font=("Verdana", 11))
        label.pack(side="top", fill="x", pady=10, padx=10)
        
        fig, ax = plt.subplots()
        im = ax.imshow(img, origin='upper')
        plt.grid("off")
        canvas = FigureCanvasTkAgg(fig, popup_lr)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
        label.pack(side="top", pady=2, padx=30)
        
    elif disease=='Grape___Esca_(Black_Measles)':
        img = io.imread(ab)
        label = ttk.Label(popup_lr, justify=tk.CENTER,
                  text="Grape___Esca_(Black_Measles)", font=("Verdana", 11))
        label.pack(side="top", fill="x", pady=10, padx=10)
        fig, ax = plt.subplots()
        im = ax.imshow(img, origin='upper')
        plt.grid("off")
        canvas = FigureCanvasTkAgg(fig, popup_lr)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
        label.pack(side="top", pady=2, padx=30)
        
    elif disease=='Orange___Haunglongbing_(Citrus_greening)':
        img = io.imread(ab)
        label = ttk.Label(popup_lr, justify=tk.CENTER,
                  text="Orange___Haunglongbing_(Citrus_greening)", font=("Verdana", 11))
        label.pack(side="top", fill="x", pady=10, padx=10)
        fig, ax = plt.subplots()
        im = ax.imshow(img, origin='upper')
        plt.grid("off")
        canvas = FigureCanvasTkAgg(fig, popup_lr)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
        label.pack(side="top", pady=2, padx=30)
        
    elif disease=='Grape___Healthy':
        img = io.imread(ab)
        label = ttk.Label(popup_lr, justify=tk.CENTER,
                  text="Grape___Healthy", font=("Verdana", 11))
        label.pack(side="top", fill="x", pady=10, padx=10)
        fig, ax = plt.subplots()
        im = ax.imshow(img, origin='upper')
        plt.grid("off")
        canvas = FigureCanvasTkAgg(fig, popup_lr)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
        label.pack(side="top", pady=2, padx=30)
    
    else:
        img = io.imread(ab)
        label = ttk.Label(popup_lr, justify=tk.CENTER,
                  text="Peach__Healthy", font=("Verdana", 11))
        label.pack(side="top", fill="x", pady=10, padx=10)
        fig, ax = plt.subplots()
        im = ax.imshow(image, origin='upper')
        plt.grid("off")
        canvas = FigureCanvasTkAgg(fig, popup_lr)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        label = ttk.Label(popup_lr, justify=tk.CENTER, text="",)
        label.pack(side="top", pady=2, padx=30)
        

    
    popup_lr.mainloop()

if __name__=="__main__":
    final(ab)

