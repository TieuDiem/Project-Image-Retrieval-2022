import tensorflow as tf 
import sys,os
import numpy as np

from tensorflow.keras.preprocessing import image as kimage
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg19 import preprocess_input

from tensorflow.keras.applications import EfficientNetB0 
from tensorflow.keras.applications import EfficientNetB1
from tensorflow.keras.applications import EfficientNetB2 
from tensorflow.keras.applications import EfficientNetB3 
from tensorflow.keras.applications import EfficientNetB4 
from tensorflow.keras.applications import EfficientNetB5
from tensorflow.keras.applications import EfficientNetB6
from tensorflow.keras.applications import EfficientNetB7 


print(f'tensorflow version; {tf.__version__}')
sys.path.append(os.getcwd())

class ExtractFeature():
    def __init__(self,mode_name):
        
        if mode_name =="vgg16" or mode_name =="vgg19":
            self.size = (128,128)
            self.output_size =(4,4)
            self.model = tf.keras.applications.VGG16(include_top=False, 
                                    weights='imagenet', 
                                    input_shape=(128, 128, 3))

        elif mode_name =="vgg19":
            
            self.size = (224,224)
            self.model = tf.keras.applications.VGG19(include_top=False, 
                                    weights='imagenet', 
                                    input_shape=(224, 224, 3))
            
        elif mode_name =="b0":
            self.output_size =(7,7)
            self.size = (224,224)
            self.model = tf.keras.applications.EfficientNetB0(include_top=False, 
                                        weights='imagenet', 
                                        input_shape=(224, 224, 3))
            
        elif mode_name =="b1":
            self.size = (240,240)
            self.model = tf.keras.applications.EfficientNetB1(include_top=False, 
                            weights='imagenet', 
                            input_shape=(240, 240, 3))
            
        elif mode_name =="b2":
            self.size = (260,260)
            self.model = tf.keras.applications.EfficientNetB2(include_top=False, 
                            weights='imagenet', 
                            input_shape=(260, 260, 3))
            
        elif mode_name =="b3":
            self.size = (300,300)
            self.model = tf.keras.applications.EfficientNetB2(include_top=False, 
                            weights='imagenet', 
                            input_shape=(300, 300, 3))
            
        elif mode_name =="b4":
            self.size = (380,380)
            self.model = tf.keras.applications.EfficientNetB4(include_top=False, 
                            weights='imagenet', 
                            input_shape=(380, 380, 3))
            
        elif mode_name =="b5":
            self.size = (456,456)
            self.model = tf.keras.applications.EfficientNetB5(include_top=False, 
                            weights='imagenet', 
                            input_shape=(456, 456, 3))
            
        elif mode_name =="b6":
            self.size = (528,528)
            self.model = tf.keras.applications.EfficientNetB6(include_top=False, 
                            weights='imagenet', 
                            input_shape=(528, 528, 3))
            
        elif mode_name =="b7":
            self.size = (600,600) 
            self.model = tf.keras.applications.EfficientNetB7(include_top=False, 
                            weights='imagenet', 
                            input_shape=(600, 600, 3))
              
        self.model.summary()    
      
        
    def compute_feature_map(self,path_img_query):
        query = kimage.load_img(path_img_query, target_size=self.size)        
        query = kimage.img_to_array(query)          # (128,128,3)
        query_np = np.expand_dims(query, axis=0)    # (1, 128,128,3) Expand dim of array
        image_feature_map = self.model.predict(query_np,verbose=0)
    
        return  image_feature_map
    
    def folder_to_images_deep(self,folder):
        
        list_dir = [folder + '/' + name for name in os.listdir(folder) if name.endswith((".jpg", ".png", ".jpeg"))]
        i = 0
        
        images_np = np.zeros(shape=(len(list_dir), * self.output_size, 512))
        images_path = []
        for path in list_dir:
            try:
                temp = self.compute_feature_map(path)
                temp= temp[0,0:,0:,0:]
                images_np[i] = temp
                images_path.append(path)
                i += 1
            except Exception:
                print("error: ", path)
                os.remove(path)

        images_path = np.array(images_path)
        return images_np, images_path
    
