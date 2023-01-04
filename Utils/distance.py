import numpy as np

from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

__all__ =[
    
    "compute_abs",
    "compute_mean_square_error",
    "compute_cosine_similarity",
    "compute_correlation_cofficient",
    
    "cal_abs",
    "cal_mean_square_error",
    "cal_cosine_similarity",
    "cal_correlation_coefficient"    
]

__doc__="""

Class Supported method calculate distace between 2 array or between tensorflow

"""

# -------------------------------- Calculate while input is tensor variable --------------------------------
def compute_abs(image1_features:np.ndarray, 
                image2_features:np.ndarray ):
    image1_features = np.reshape(image1_features, (-1,)).astype(np.float32)
    abs =[]
    for i in range(0,image2_features.shape[0]):
        _features = np.reshape(image2_features[i]).astype(np.float32)
        _abs = np.absolute(image1_features, _features).mean()
        abs.append(_abs)
        
    return abs


def compute_mean_square_error(image1_features:np.ndarray, 
                             image2_features:np.ndarray ):
    image1_features = np.reshape(image1_features, (1, -1)).astype(np.float32)
    mse =[]
    for i in range(0,image2_features.shape[0]):
        _features = np.reshape(image2_features[i], (1, -1)).astype(np.float32)
        _mse = mean_squared_error(image1_features,_features)
        mse.append(_mse)
        
    return mse


def compute_cosine_similarity(image1_features:np.ndarray, 
                             image2_features:np.ndarray ):
    image1_features = np.reshape(image1_features, (1, -1)).astype(np.float32)
    sims =[]
    for i in range(0,image2_features.shape[0]):
        _features = np.reshape(image2_features[i], (1, -1)).astype(np.float32)
        _sims = cosine_similarity(image1_features, _features).squeeze()
        sims.append(_sims)
        
    return sims


def compute_correlation_cofficient(image1_features:np.ndarray, 
                                    image2_features:np.ndarray ):
    image1_features = np.reshape(image1_features, (-1,)).astype(np.float32)
    corr =[]
    for i in range(0,image2_features.shape[0]):
        _features = np.reshape(image2_features[i], (-1,)).astype(np.float32)

        _corr = pearsonr(image1_features, _features)[0]
        corr.append(_corr)
        
    return corr

# -------------------------------- Calculate while input is numpy variable --------------------------------

def cal_abs(query:np.ndarray, 
            X:np.ndarray):
    
    axis_batch_size = tuple(range(1,len(X.shape)))
    abs = np.sum(np.abs(X - query), axis=axis_batch_size)
    return abs


def cal_mean_square_error(query:np.ndarray, 
                          X:np.ndarray):
    
    axis_batch_size = tuple(range(1,len(X.shape)))
    mse = np.mean((X - query)**2, axis=axis_batch_size)  
    return  mse   


def cal_cosine_similarity(query:np.ndarray, 
                          X:np.ndarray):
    
    axis_batch_size = tuple(range(1,len(X.shape)))
    query_norm = np.sqrt(np.sum(query**2))
    X_norm = np.sqrt(np.sum(X**2, axis=axis_batch_size))
    cosim = np.sum(X * query, axis=axis_batch_size) /(query_norm*X_norm + np.finfo(float).eps)
    return cosim

      
def cal_correlation_coefficient(query:np.ndarray,
                                X:np.ndarray):
    
    axis_batch_size = tuple(range(1,len(X.shape)))
    
    query_mean = query - np.mean(query)
    X_mean = X - np.mean(X, axis=axis_batch_size, keepdims=True)
    
    query_norm = np.sqrt(np.sum(query_mean**2))
    X_norm = np.sqrt(np.sum(X_mean**2, axis=axis_batch_size))
    
    corr=  np.sum(X_mean * query_mean, axis=axis_batch_size) / (query_norm*X_norm +np.finfo(float).eps)
    return corr