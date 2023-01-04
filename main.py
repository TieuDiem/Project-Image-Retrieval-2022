__all__ = [
    
    """_summary_
    """
]

__doc__ =[
    
    """_summary_
    link dowload images data : "https://www.freeimages.com/search/{name}/"
    
    PrepareData is class supported image and extract feature map -> save feature map file
    
    QuerryExe is class supported the quering image from input image with mode:
    
        * Using original distance (l1, l2, cosine similarity, correlation cofficient)
        * Using CNN  + original distance (l1, l2, cosine similarity, correlation cofficient)
    """ 
]

import os
from Utils.prepareData import PrepareData
from Utils.query import QueryExe

root_img_path       = "images/"
query_path          = os.path.join("image_query","img2.jpg")
            
if __name__== "__main__":
    
    #_  = PrepareData()()
    _  = QueryExe(  query_mode=1 ,
                    root_img_path =root_img_path,
                    query_path =query_path,
                    distance ="l1",
                    first_run =False)()

    print(f'sucessfully...')
    