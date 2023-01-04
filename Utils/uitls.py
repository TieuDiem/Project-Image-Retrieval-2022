
import os
import sys
import numpy as np
from PIL import Image
sys.path.append(os.getcwd())

from Utils.crawData import GetImagesfromPages
from Utils.dowloadData  import DownloadImagesFromUrls

__all__=[
    "urls_to_txts",
    "dowload_image_from_txts",
    "processing_data",
    "read_image_from_path",
    "folder_to_images",
    "extract_path_from_folder"
]
__doc__="""

Class supported method with purpose dowload image and save to disk 
Class supported load all of image path in the folder
"""
def urls_to_txts(topic_names,topics,urltopic,n_page,n_threads):
        for dir, names in zip(topic_names,topics):
            dir_path_urls  = f'data/{dir}/urls'
            if not os.path.exists(dir_path_urls):
                os.makedirs(dir_path_urls)
            
            for name in names :
                result_of_name = []
                for key in urltopic.keys():
                    res  = GetImagesfromPages(min(n_threads, n_page//2), n_page, 
                                urltopic[key].format(name = name))()
                    
                    if len(res) > 0:
                        res = list(set(res))
                        result_of_name.extend(res)
                print(f"{dir_path_urls}/{dir}_{name}.txt have {len(result_of_name)}images \n")

                strResult = "\n".join(result_of_name)
                with open(f"{dir_path_urls}/{dir}_{name}.txt", "w") as f:
                    f.write(strResult)

def dowload_image_from_txts(topic_names, topics):
    for dir, names in zip(topic_names, topics):

        dir_path_images = f"images"
        dir_path_urls = f"data/{dir}/urls"
        if not os.path.exists(dir_path_images):
            os.makedirs(dir_path_images)

        txts = [name for name in os.listdir(dir_path_urls) if name.endswith(".txt")]

        for txt in txts:
            folder_txt = f"{dir_path_urls}/{txt}"
            with open(folder_txt, "r") as f:
                content_txt = f.readlines()

            folder_image = f"{dir_path_images}/{txt}"
            if not os.path.exists(folder_image[:-4]):
                os.makedirs(folder_image[:-4])
            print(folder_image[:-4])
            
            n_threads = 10
            DownloadImagesFromUrls(min(n_threads, len(content_txt)//2), 
                                   content_txt, 
                                   folder_image[:-4])()
            
def processing_data(images_path):
    dic_categories = {
        'animal' : [], 
        'plant' : [], 
        'furniture' : [], 
        'scenery' : []
        }
    count = 0
    
    for folder in os.listdir(images_path):
        if folder.split("_")[0] in dic_categories:
            path = images_path + folder
            list_dir = [path + '/' + name for name in os.listdir(path) if name.endswith((".jpg", ".png", ".jpeg"))]
            for p in list_dir:
                try:
                    img = Image.open(p) 
                    img.verify() # verify that it is, in fact an image
                    img = Image.open(p) 
                    if img.width < 10:
                        print("Image too small: ", p)
                        os.remove(p) 
                    
                    img = np.asarray(img)
                    if img.shape[2] != 3:
                        os.remove(p) 

                except Exception as e:
                    print(e)
                    count += 1
                    print("error: ", p)
                    os.remove(p)

def read_image_from_path(path, size):
    im = Image.open(path).resize(size) 
    return np.asarray(im, dtype=np.float32)

def folder_to_images(folder,size):
    
    list_dir = [folder + '/' + name for name in os.listdir(folder) if name.endswith((".jpg", ".png", ".jpeg"))]
    
    i = 0
    images_np = np.zeros(shape=(len(list_dir), *size, 3))
    images_path = []
    for path in list_dir:
        try:
            images_np[i] = read_image_from_path(path, size)
            images_path.append(path)
            i += 1
                        
        except Exception:
            print("error: ", path)
            os.remove(path)

    images_path = np.array(images_path)
    return images_np, images_path

def extract_path_from_folder(folder):
    list_dir = [folder + '/' + name for name in os.listdir(folder) if name.endswith((".jpg", ".png", ".jpeg"))]
    i = 0
    images_path = []
    for path in list_dir:
        try:
            images_path.append(path)
            i += 1
        except Exception:
            print("error: ", path)
            os.remove(path)

    images_path = np.array(images_path)
    return images_path