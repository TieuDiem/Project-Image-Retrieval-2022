import os 
import sys

sys.path.append(os.getcwd())

from Utils.getScore import get_ditance_score
from Utils.getScore import get_ditance_score_deep
from Utils.imShow import plot_results
__all__ =[
    
    "__call__"
]
__doc__="""

Class supported some methods calculate distance of query's feature map and data image
"""
class QueryExe():
    def __init__(self,query_mode,root_img_path,query_path,
                 distance,first_run):
        
        self.mode= query_mode
        self.root_img_path=root_img_path
        self.query_path =query_path
        self.distance =distance
        self.first_run =first_run
        
    def __call__(self):
        
        if self.mode ==1:
            size = (448, 448)
            query, ls_path_score = get_ditance_score(self.root_img_path, 
                                                     self.query_path, 
                                                     size,
                                                     distance = self.distance,
                                                     first_run= self.first_run )
            plot_results(query, ls_path_score)
           
        elif self.mode ==2 :
            query, ls_path_score = get_ditance_score_deep(self.root_img_path, 
                                                          self.query_path, 
                                                          distance = self.distance,
                                                          first_run=self.first_run )
            plot_results(query, ls_path_score) 
           
       
       
    
     
    

       