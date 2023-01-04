import os
import sys

sys.path.append(os.getcwd())

from config  import animal_class,plant_class,furniture_class,scenery_class
from Utils.uitls  import  urls_to_txts 
from Utils.uitls  import  dowload_image_from_txts
from Utils.uitls  import  processing_data      

__doc__ =="""

Class supported craw path of image from web based on src path
Class supported dowload image based on url of image source
Class supported delete image invalid (width < 10, num of channel !=3)
"""

class PrepareData():
    
    def __init__(self):
        pass
    
    def __call__(self):
        
        urltopic = {
            
            "freeimages": "https://www.freeimages.com/search/{name}/"
        }

        topic_names = ["animal", "plant", "furniture", "scenery"]

        topics = [animal_class, plant_class,  furniture_class, scenery_class]
                    
        n_threads = 5;n_page = 2
        
        urls_to_txts(topic_names=topic_names, 
                     topics=topics, 
                     urltopic=urltopic, 
                     n_page=n_page, 
                     n_threads=n_threads)   
        
        dowload_image_from_txts(topic_names=topic_names, topics=topics)
        processing_data(images_path= os.path.join(os.getcwd() ,"images/"))
        
        return (f'Prepare Data Successfully ...')