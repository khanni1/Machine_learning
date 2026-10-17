from sklearn.datasets import load_iris
import pandas as pd
import ml_module as ml

ir = load_iris()

data = pd.DataFrame(data = ir.data , columns = ir.feature_names)

mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

tar = ir.target

# print(data,tar)




print(mapper[ml.knn(data,[5.0, 3.5, 1.4, 0.3],tar,3,1)])

# print(data.iloc[34])
# print(data.iloc[45])
    
    
        
    








