import os
import random
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
from PIL import Image

class predict_class:
    # ------------------------------------------------------

    def __init__(self, model):
        self.model = model
        self.class_names = ['daisy 🌼', 'dandelion 🏵️', 'rose 🌹', 'sunflower 🌻', 'tulip 🌷']

        dir = 'train/rose/'
        self.train_rose = [dir + file for file in os.listdir('train/rose') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'train/daisy/'
        self.train_daisy = [dir + file for file in os.listdir('train/daisy') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'train/dandelion/'
        self.train_dandelion = [dir + file for file in os.listdir('train/dandelion') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'train/sunflower/'
        self.train_sunflower = [dir + file for file in os.listdir('train/sunflower') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'train/tulip/'
        self.train_tulip = [dir + file for file in os.listdir('train/tulip') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        dir = 'test/rose/'
        self.test_rose = [dir + file for file in os.listdir('test/rose') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'test/daisy/'
        self.test_daisy = [dir + file for file in os.listdir('test/daisy') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'test/dandelion/'
        self.test_dandelion = [dir + file for file in os.listdir('test/dandelion') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'test/sunflower/'
        self.test_sunflower = [dir + file for file in os.listdir('test/sunflower') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'test/tulip/'
        self.test_tulip = [dir + file for file in os.listdir('test/tulip') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        dir = 'val/rose/'
        self.val_rose = [dir + file for file in os.listdir('val/rose') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'val/daisy/'
        self.val_daisy = [dir + file for file in os.listdir('val/daisy') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'val/dandelion/'
        self.val_dandelion = [dir + file for file in os.listdir('val/dandelion') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'val/sunflower/'
        self.val_sunflower = [dir + file for file in os.listdir('val/sunflower') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        dir = 'val/tulip/'
        self.val_tulip = [dir + file for file in os.listdir('val/tulip') 
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        self.all_dir = [self.train_daisy, self.train_dandelion, 
                        self.train_rose, self.train_sunflower, self.train_tulip, 
                        
                        self.test_daisy, self.test_dandelion, 
                        self.test_rose, self.test_sunflower, self.test_tulip, 
                        
                        self.val_daisy, self.val_dandelion, 
                        self.val_rose, self.val_sunflower, self.val_tulip]
    # ------------------------------------------------------

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
    
    # ------------------------------------------------------
    
    def image_load_dir(self):
        # Chooses a random image and it's class
        dir = random.choice(self.all_dir)
        photo = random.choice(dir)
        actual_class = photo.split("/")[1]

        # Imports the image 
        img_width, img_height = 150, 150
        img = image.load_img(photo, target_size = (img_width, img_height))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis = 0)

        # Return image and class
        return (photo, img, actual_class)


    def predict_flower_dir(self, n):
        results = []
        for i in range(n):
            result_dict = {}

            img_dir, img, act_class = self.image_load_dir()
            pred = self.model.predict(img)[0]

            for i in range(5):
                result_dict[self.class_names[i]] = pred[i]
            pred_class = self.dict_max(result_dict)

            temp = (img_dir, result_dict, pred_class, act_class)
            results.append(temp)

        return results
    
