import pandas as pd
import matplotlib.pyplot as plt
import ml_module as ml

from sklearn.datasets import load_iris

ir = load_iris()

data = pd.DataFrame(data = ir.data , columns = ir.feature_names)

data['tar'] = ir.target

mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'} 
# for mapping classes

data_len = len(data)

trains = int(0.8*data_len)
tests = int(0.2*data_len)

training = data.sample(trains)

testing = data.sample(tests)


wrong = {}

for k in range(1,16,2):
    wrongs = 0
    for t in range(0,tests):
        prediction = ml.knn(training.drop(columns='tar') , list(testing.iloc[t].drop(columns='tar')) ,training['tar'],k,1)
        if prediction != testing.iloc[t]['tar']:
            wrongs += 1
            
    wrong[k] = wrongs
    
print(wrong)
        
        
            
    



