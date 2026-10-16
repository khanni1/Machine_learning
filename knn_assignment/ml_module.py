import pandas as pd
import numpy as np
import matplotlib as plt

def distance(a:list,b:list,n,p=2):
    # n dimensionals points an
    summ = 0
    for i in range(0,n):
        summ = summ + abs(a[i] - b[i])**p
        
    return summ**(1/p)


def knn(df,qp,tar,mapper,k=3,p=2):
    m = df.shape[0]
    n = df.shape[1]
    
    d = []

    
    for i in range(0,m):
        d.append(distance(list(df.iloc[i]),qp,n,p))
        
    res = pd.DataFrame({'distances' : d,'Y' : tar})
    
    res = res.sort_values(by = 'distances')
    # -------------------------------------------------------------------
    freq = {}
    temp = list(res[0:k]['Y'])
    for i in range(0,len(temp)):
        mapped = mapper[temp[i]]
        if mapped in freq:
            freq[mapped] += 1 
        else:
            freq[mapped] = 1
            
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

    
    return res[0:k],freq
