from sklearn.datasets import load_iris
import pandas as pd
import khdistance as kh

ir = load_iris()

data = pd.DataFrame(data = ir.data , columns = ir.feature_names)

mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

tar = ir.target

print(data,tar)

def knn(df,qp,tar,k=3,p=2):
    m = df.shape[0]
    n = df.shape[1]
    
    d = []

    
    for i in range(0,m):
        d.append(kh.distance(list(df.iloc[i]),qp,n,p))
        
    res = pd.DataFrame({'distances' : d,'Y' : tar})
    
    res = res.sort_values(by = 'distances')
    
    return res[0:k]


print(knn(data,[6.2,3.4,5.4,2.3],tar))

# print(data.iloc[34])
# print(data.iloc[45])
    
    
        
    








