import pandas as pd
import numpy as np

def mean_normalise(x,type = 1):
    mu = np.mean(x)
    range = max(x) - min(x)
    stddev = np.std(x)
    
    # clamp case
    if(range == 0):
        range = min(x)
    if(stddev == 0):
        stddev = min(x)
    
    if (type):
        xn = (x - mu)/range
    else:
        xn = (x-mu)/stddev
    
    return xn

'''
if i/p in this form 
rows as records (i) till m
and cols as features (j) till n (1 added as x0) 

x = np.array([
    [1,  2.1,  1.0,  0.5,  3.2],
    [1,  1.5,  2.3,  1.1,  2.8],
    [1,  3.2,  0.7,  0.2,  4.1],
    [1,  0.8,  1.9,  2.4,  1.0],
    [1,  2.9,  1.2,  0.9,  3.6],
    [1, -0.5,  2.8,  1.7,  0.4],
'''

def bulk_scale(x):
    x = x.T
    
    m = len(x[1])
    n = len(x)
    
    
    x_fs = np.zeros((n,m))
    

    for j in range(0,n):
        x_fs[j] = mean_normalise(x[j])
        
    return (x_fs.T)
