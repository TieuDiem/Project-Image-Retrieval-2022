import os 
import sys
from PIL import Image
import numpy as np
from tqdm import tqdm
sys.path.append(os.getcwd())
from Utils.uitls import read_image_from_path
from Utils.uitls import folder_to_images
from Utils.uitls import extract_path_from_folder

from Utils.distance import cal_abs
from Utils.distance import cal_mean_square_error
from Utils.distance import cal_cosine_similarity
from Utils.distance import cal_correlation_coefficient

from Utils.distance import compute_abs
from Utils.distance import compute_mean_square_error
from Utils.distance import compute_cosine_similarity
from Utils.distance import compute_correlation_cofficient

from Utils.extractFeature import ExtractFeature

__all__=[
    
    "get_ditance_score",
    "get_ditance_score_deep"
]

def get_ditance_score(root_img_path, query_path, size,distance = "l1",first_run=True):
    if distance =="l1":
        _distance = cal_abs
        
    elif distance =="l2":
        _distance = cal_mean_square_error
        
    elif distance =="cosine":
        _distance = cal_cosine_similarity
        
    elif distance =="corr":
        _distance = cal_correlation_coefficient
      
    dic_categories = ['scenery', 'furniture', 'animal', 'plant'] 
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in tqdm(os.listdir(root_img_path)):
        if folder.split("_")[0] in dic_categories:
            path = root_img_path + folder
            if first_run:
                images_np, images_path = folder_to_images(path, size) 
                np.save(os.path.join(path,'feature_normal'),images_np)
            else :
                images_np =np.load(os.path.join(path,'feature_normal.npy'))
                images_path = extract_path_from_folder(path)
            rates = _distance(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score


def get_ditance_score_deep(root_img_path, query_path,distance = "l1",first_run =True):
    if distance =="l1":
        _distance = compute_abs
        
    elif distance =="l2":
        _distance = compute_mean_square_error
        
    elif distance =="cosine":
        _distance = compute_cosine_similarity
        
    elif distance =="corr":
        _distance = compute_correlation_cofficient
      
    dic_categories = ['scenery', 'furniture', 'animal', 'plant'] 
    
    extract =ExtractFeature("vgg16")
    
    query = extract.compute_feature_map(query_path)
    
    im = Image.open(query_path).resize(extract.size) 
    
    ls_path_score = []
    for folder in tqdm(os.listdir(root_img_path)):
        if folder.split("_")[0] in dic_categories:
            path = root_img_path + folder
            if first_run:
                images_np, images_path = extract.folder_to_images_deep(path) 
                np.save(os.path.join(path,'feature_deep'),images_np)
            else:    
                images_np =np.load(os.path.join(path,'feature_deep.npy'))
                images_path = extract_path_from_folder(path)
            rates = _distance(query, images_np)
            
            ls_path_score.extend(list(zip(images_path, rates)))
            
    return  np.asarray(im, dtype=np.float32), ls_path_score

