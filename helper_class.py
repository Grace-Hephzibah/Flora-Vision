import os
import random
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

class predict_class:
    def __init__(self, model):
        self.model = model
        self.class_names = ['daisy 🌼', 'dandelion 🏵️', 'rose 🌹', 'sunflower 🌻', 'tulip 🌷']

    def image_load_dir(self, dir):
        img_width, img_height = 150, 150
        img = image.load_img(dir, target_size = (img_width, img_height))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis = 0)
        return img

    def predict_flower_dir(self, dir):
        result_dict = {}
        img = self.image_load_dir(dir)
        pred = self.model.predict(img)[0]
        for i in range(5):
            result_dict[self.class_names[i]] = pred[i]
        return result_dict
    
    # Choosing random images 
    def choose_random_images(self, directory_path):
        image_files = [file for file in os.listdir(directory_path) 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        selected_image = random.sample(image_files, 1)
        image_path = os.path.join(directory_path, selected_image )
        return image_path

    def dict_max(self, dic):
        max_key = 0
        max_val = 0
        for key in dic:
            val = dic[key]
            if val>max_val:
                max_val = val
                max_key = key
        return max_key

    def predict_flower(self, img):
        result_dict = {}
        pred = self.model.predict(img)[0]
        for i in range(5):
            result_dict[self.class_names[i]] = pred[i]

        pred_class = self.dict_max(result_dict)
        return result_dict
    
