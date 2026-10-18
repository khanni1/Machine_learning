import pandas as pd
import matplotlib.pyplot as plt
import ml_module as ml

from sklearn.datasets import load_iris

ir = load_iris()

data_original = pd.DataFrame(data = ir.data , columns = ir.feature_names)

data_original['tar'] = ir.target

data = data_original.sample(frac=1).reset_index(drop=True) # shuffle the dataset


mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'} 
# for mapping classes

data_len = len(data)

trains = int(0.8*data_len)
tests = int(0.2*data_len)

training = data.head(trains)
testing = data.tail(tests)


wrong = {}

x_testing = testing.drop(columns='tar')
x_training = training.drop(columns='tar')

for k in range(1,16,2):
    wrongs = 0
    for t in range(0,tests):
        prediction = ml.knn(x_training , list(x_testing.iloc[t]) ,training['tar'],k,1)
        if prediction != testing.iloc[t]['tar']:
            wrongs += 1
            
    wrong[k] = wrongs
    
print(wrong)
        
        
            
    



