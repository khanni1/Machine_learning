from sklearn.datasets import load_iris
import pandas as pd
import ml_module as ml

ir = load_iris()
data = pd.DataFrame(data = ir.data , columns = ir.feature_names)
tar = ir.target
mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}


df,ans = ml.knn(data,[6.2,3.4,5.4,2.3],tar,mapper,50)

print(df)
print(ans)


# print(data.iloc[34])
# print(data.iloc[45])
    
    
        
    








