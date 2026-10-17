from sklearn.datasets import load_iris
import pandas as pd
import ml_module as ml

ir = load_iris()

data = pd.DataFrame(data = ir.data , columns = ir.feature_names)

mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

train_tar = ir.target

# print(data,tar)


    

print(mapper[ml.knn(data,[5.0, 3.5, 1.4, 0.3],train_tar,3,1)])
print(mapper[ml.knn(data,[10,10,10,10],train_tar,3,1)])
print(mapper[ml.knn(data,[6.6, 3.0, 5.5, 2.0],train_tar,3,1)])

print(mapper[ml.knn(data,[6.0, 2.7, 5.1, 1.6],train_tar,1,1)])
print(mapper[ml.knn(data,[6.0, 2.7, 5.1, 1.6],train_tar,3,1)])


    
    
        
    








