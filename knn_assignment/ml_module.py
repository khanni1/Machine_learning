import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def distance(a:list,b:list,n,p=2):
    # n dimensionals points an
    summ = 0
    for i in range(0,n):
        summ = summ + abs(a[i] - b[i])**p
        
    return summ**(1/p)

def knn(df,qp,tar,k=3,otype = 0,p=2):
    m = df.shape[0]
    n = df.shape[1]
    
    d = []

    
    for i in range(0,m):
        d.append(distance(list(df.iloc[i]),qp,n,p))
        
    res = pd.DataFrame({'distances' : d,'Y' : tar})
    
    res = res.sort_values(by = 'distances')
    
    res = res[0:k] #first k of sorted records
    
    if(otype == 0):
        return res
    elif(otype == 1):
        return res['Y'].mode()[0]
        
    