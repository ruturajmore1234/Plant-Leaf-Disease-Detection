# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:43:53 2019

@author: m0rem0rem0re


"""



import datetime
import pickle
import json
from django.shortcuts import render
from django.http import HttpResponse
import cv2
import numpy
from custom_code import image_converter

import io
import base64
import numpy as np
from PIL import Image
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg





default_image_size = tuple((256, 256))

#image = Image.open(io.BytesIO(base64.b64decode('plant.data')))
image = Image.open('tomato_leaf_mold.JPG')
plt.imshow(image)
#image = cv2.imread('tomato_healthy2.JPG')
image = image.resize(default_image_size, Image.ANTIALIAS)
#image = image.resize((256, 256), Image.ANTIALIAS)
#image = cv2.resize(image,(256,256))   
image_array = img_to_array(image)
image_array = np.expand_dims(image_array, axis=0)
model_file = f"cnn_model.pkl"
saved_classifier_model = pickle.load(open(model_file,'rb'))
prediction = saved_classifier_model.predict(image_array) 
label_binarizer = pickle.load(open(f"label_transform.pkl",'rb'))
print("The Disease detected is :" ,label_binarizer.inverse_transform(prediction)[0] )


#def predict_plant_disease(request):
#    request_data = request.data["plant.data"]
#    header, image_data = request_data.split(';base64,')
#    image_array, err_msg = image_converter.convert_image(image_data)
#    if err_msg == None :
#        model_file = f"cnn_model.pkl"
#        saved_classifier_model = pickle.load(open(model_file,'rb'))
#        prediction = saved_classifier_model.predict(image_array) 
#        label_binarizer = pickle.load(open(f"label_transform.pkl",'rb'))
#        print("[INFO] ,label_binarizer.inverse_transform(prediction)[0] ")
        
#        return_data = {
#                        "error" : "0",
#                        "data" : f"{label_binarizer.inverse_transform(prediction)[0]}"
#    }