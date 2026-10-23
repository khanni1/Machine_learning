
import numpy as np
import pandas as pd 

def sig(a,x):
    ans = 1/(1+np.exp(-z(a,x)))
    return ans



def z(a,x):
    ans = a @ x
    return ans


n = 2  #number of features

a = np.zeros(n) 
ta = np.zeros(n) 

x = np.array([
    [1,2],
    [1,4],
    [1,6],
    [1,10],
    [1,14],
])       

y = np.array([0,0,0,1,1])   

m = len(y)

al = 0.001

for k in range(0,5000):
    for j in range(0,n,1):
        summ = 0 
        for i in range(0,m,1):
            summ = summ + ((sig(a,x[i]) - y[i])*x[i][j])
        ta[j] = a[j] - ((al/m) * summ) 
    a = ta.copy()


print(a)