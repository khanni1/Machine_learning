import numpy as np
import pandas as pd 
import feature_scaler as fs

def sig(a,x):
    ans = 1/(1+np.exp(-z(a,x)))
    return ans



def z(a,x):
    ans = a @ x
    return ans


n = 5  #number of features

a = np.zeros(n) 
ta = np.zeros(n ) 

x = np.array([
    [1,  2.1,  1.0,  0.5,  3.2],
    [1,  1.5,  2.3,  1.1,  2.8],
    [1,  3.2,  0.7,  0.2,  4.1],
    [1,  0.8,  1.9,  2.4,  1.0],
    [1,  2.9,  1.2,  0.9,  3.6],
    [1, -0.5,  2.8,  1.7,  0.4],
    [1, -1.2,  3.1,  2.2,  0.9],
    [1,  0.3,  2.5,  1.9,  1.3],
    [1,  3.5,  0.4,  0.6,  3.9],
    [1, -0.9,  2.2,  2.6,  0.2],
])   


y = np.array([1, 1, 1, 0, 1, 0, 0, 0, 1, 0])   # shape (10,)

m = len(y)

x = fs.bulk_scale(x)
print(x)
       


al = 0.1

for k in range(0,100):
    for j in range(0,n,1):
        summ = 0 
        for i in range(0,m,1):
            summ = summ + ((sig(a,x[i]) - y[i])*x[i][j])
        ta[j] = a[j] - ((al/m) * summ) 
    a = ta.copy()


print(a)

#  just testing

xt = x.T 

qp = np.ones(5)



# for j in range(0,5):
#     temp = float(input(f"enter feature {j} : "))
    
#     mu = np.mean(xt[j])
    
#     range = max(xt[j]) - min(xt[j])
    
#     if (range):
#         qp[j] = (temp - mu)/range
#     else:
#         qp[j] = temp-mu
        

print(sig(a,np.array([ 1 ,-0.35531915,  0.36666667,  0.12083333, -0.44615385])))
